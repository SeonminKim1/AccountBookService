from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import UserSignUpSerializer, UserSignInSerializer
from .jwt_module import utils

class UserSignUpAPIView(APIView):
    """ 고객 회원가입 기능
    endpoint : api/user/signup
    input body : email, password, nickname
    return : user data json / status : 201, 400
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

class UserSignInAPIView(APIView):
    """ 고객 로그인 기능
    endpoint : api/user/signin
    input body : email, password
    return : token json / status : 201, 400
    - 로그인 입력 정보 DB와 일치 여부 검증 (authenticate)
    - 고객이 로그인 시 유효 시간이 있는 Access Token(10분)과 Refresh Token(3일) 발급
    - 고객이 10분 이후 재접근시 AccessToken은 만료되어 재발급 필요
    - jwt 관련 함수 설명은 jwt_module/utils.py 주석 참고
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        user_serializer = UserSignInSerializer(data=request.data)
        if user_serializer.is_valid():
            token = user_serializer.validated_data
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class UserSignOutAPIView(APIView):
    """ 고객 로그아웃
    endpoint : api/user/signout
    input body : refresh token
    return : detail msg / status : 204, 400, 401
    - 로그아웃시 발행된 토큰이 폐기(blacklist)되어 해당 Token으로 재접근이 불가능
    - 로그아웃을 하지 않고 재접근시 기존에 발급 된 Access Token이 활용
    - jwt 관련 함수 설명은 jwt_module/utils.py 주석 참고
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh = utils.check_refresh_token(request.data['refresh_token'])
        if refresh == None:
            return Response(
                {'detail':'만료된 token이거나 토큰 정보가 유효하지 않습니다.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if request.user.id != refresh['user_id']:
            return Response(
                {'detail':'유저의 토큰 정보가 유효하지 않습니다.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        utils.add_refresh_token_in_blacklist(request.user, refresh)
        return Response({'detail':'Logout 성공!'}, status=status.HTTP_204_NO_CONTENT) 