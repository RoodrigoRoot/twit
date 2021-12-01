from django.urls import path
from accounts.views import UserCreateAPIView, UserDetailAPIView, FollowCreateAPIView

urlpatterns = [
    path('', UserCreateAPIView.as_view(), name="create-user"),
    path('<str:username>/', UserDetailAPIView.as_view(), name="detail-user"),
    path('<str:username>/follows/', FollowCreateAPIView.as_view(), name='to-follow'),
]


