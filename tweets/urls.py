from tweets.views import TweetCreateAPIView, TweetListAPIView
from django.urls import path

app_name = 'tweets'

urlpatterns = [
    path('', TweetCreateAPIView.as_view(), name='create'),
    path('changes/', TweetListAPIView.as_view(), name='list')
]