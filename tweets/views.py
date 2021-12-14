from django.shortcuts import render
from tweets.serializers import TweetCreateSerializer, TweetReadSerializer
from tweets.selectors import tweet_get, tweet_list
from tweets.services import tweet_create
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class TweetCreateAPIView(APIView):

    def post(self, request):
        status_code_response = status.HTTP_201_CREATED
        serializer = TweetCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = tweet_create(serializer.data['body'], serializer.data['user'])
        if not res["results"]:
            status_code_response = status.HTTP_400_BAD_REQUEST
            return Response({"message": res["message"]},status=status_code_response)
        return Response(status=status_code_response)


class TweetListAPIView(APIView):

    def get(self, request):
        data = tweet_list()
        serializer = TweetReadSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

