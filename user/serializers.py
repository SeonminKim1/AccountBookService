from rest_framework import serializers
from django.contrib.auth import authenticate
from .jwt_module import utils
from .models import User
import re

class UserSignUpSerializer(serializers.ModelSerializer):
    '''고객 회원가입
    - 이메일 유효성 검사 : 중복 여부, 이메일 형식 여부 (EmailField)
    - 닉네임 유효성 검사 : 중복 여부, 4~15자리 문자열, 공백 미포함
    - 비밀번호 형식 유효성 검사 : 8~20자리 내외, 영문, 숫자, 특수기호의 1글자 이상 조합 여부
    '''
    class Meta:
        model = User
        fields = ['email', 'nickname', 'password', 'is_active', 'is_admin']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    '''
    Email is validated by EmailField in models.py
    '''

    def validate_nickname(self, data):
        if len(data.split()) >= 2:
            raise serializers.ValidationError("닉네임에 공백이 존재합니다.")
        return data

    def validate_password(self, data):
        pwd_regex = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,20}$'
        if not re.match(pwd_regex, data):
            raise serializers.ValidationError("패스워드가 형식에 맞지 않습니다.")
        return data

class UserSignInSerializer(serializers.ModelSerializer):
    '''고객 로그인
    - 고객이 로그인 시 유효 시간이 있는 Access Token(10분)과 Refresh Token(3일) 발급
    - 고객이 10분 이후 재접근시 AccessToken은 만료되어 재발급 필요
    '''
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'is_admin']

    def validate(self, data):
        user = authenticate(
            email=data['email'],
            password=data['password']
        )
        if not user: 
            raise serializers.ValidationError('잘못 된 로그인 정보를 입력하였습니다.')

        # Generate Token
        token = utils.generate_token(user)
        return token
    
    class Meta:
        model  = User
        fields = [
            'email', 'password'
        ]