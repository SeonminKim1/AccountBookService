from django.urls import path
from user.views import UserSignUpAPIView, UserSignInAPIView, UserSignOutAPIView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('signup', UserSignUpAPIView.as_view(), name='user-signup'),
    path('signin', UserSignInAPIView.as_view(), name='user-signin'),
    path('signout', UserSignOutAPIView.as_view(), name='user-signin'),
    path('token/refresh', TokenRefreshView.as_view(), name='user-token-refresh'),
]