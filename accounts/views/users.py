from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import CreateUserSerializer, ReadDataUserSerializer, UpdateDataUserSerializer
from accounts.services import user_create, user_delete, user_update
from accounts.selectors import get_user


# Create your views here.


class UserCreateAPIView(APIView):

    def post(self, request):
        print(request.data)
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_create(serializer.data)
        return Response(status=status.HTTP_201_CREATED)


class UserDetailAPIView(APIView):

    def get(self, request, username):
        user = get_user(username, True)
        serializer = ReadDataUserSerializer(data=user.__dict__)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, username):
        status_code = ""
        status_delete, message = user_delete(username)
        status_code = status.HTTP_400_BAD_REQUEST
        if status_delete:
            status_code = status.HTTP_204_NO_CONTENT

        return Response({"message": message}, status=status_code)

    def put(self, request, username):
        body = request.data
        serializer = UpdateDataUserSerializer(data=body)
        serializer.is_valid(raise_exception=True)
        user_update(username, serializer.data)
        return Response({"message": "Usuario actualizado exitosamente."}, status=status.HTTP_200_OK)

