from django.urls import path
from user.views import UserSignUpAPIView


urlpatterns = [
    path('signup', UserSignUpAPIView.as_view(), name='user-signup'),
]