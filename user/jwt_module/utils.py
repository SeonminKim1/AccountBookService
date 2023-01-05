from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken

'''
향후 재사용성을 위한 module 분리
- generate_token : token 생성 or 재생성
- add_refresh_token_in_blacklist : 로그아웃 시 발급된 토큰들 Blacklist에 등록
- check_refresh_token : token 유효 여부 체크 
'''
def generate_token(user):
    refresh_token = RefreshToken.for_user(user)
    token = {
        'refresh_token' : str(refresh_token),
        'access_token' : str(refresh_token.access_token)
    }
    return token

def check_refresh_token(token):
    try:
        refresh_token = RefreshToken(token)
    except:
        refresh_token = None
    return refresh_token

def add_refresh_token_in_blacklist(user, token):
    for token in OutstandingToken.objects.filter(user_id=user.id):
        BlacklistedToken.objects.get_or_create(token=token)