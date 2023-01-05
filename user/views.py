from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions, serializers
from rest_framework import permissions
from .serializers import UserSignUpSerializer

# api/user/signup
class UserSignUpAPIView(APIView):
    """ 고객 회원가입 기능
    input body : email, password, nickname
    return : json
    - 이메일, 비밀 번호, 닉네임 입력을 통해 가입
    - 유효성 검사는 models과 serializer에서 주로 이루어짐
    - 비밀번호는 암호화되어 저장
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        user_serializer = UserSignUpSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        # 유효성검사 통과 x
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 