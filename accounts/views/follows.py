from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.services.follows import following_create


class FollowCreateAPIView(APIView):

    def post(self, request, username):
        following = following_create(user=username, to_follow=request.data['to_follow'])
        return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
