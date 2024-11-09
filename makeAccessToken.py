# Access Token 만드는 방법. 아래 라이브러리를 설치한 다음 사용할 것
# pip install --upgrade google-auth
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
# 서비스 계정으로 자격 증명 인증
credentials = service_account.Credentials.from_service_account_file("<파이어베이스의 서비스 계정 탭에서 다운로드 받은 비공개 키의 위치 및 파일명>.json", scopes=scopes)

# Use the credentials object to authenticate a Requests session.
# 자격 증명 개체를 사용하여 요청 세션을 인증합니다.
authed_session = AuthorizedSession(credentials)
response = authed_session.get("https://<파이어베이스 리얼타임 데이터베이스 이름>.firebaseio.com/users/ada/name.json")

# 아래의 access_token 변수에 들어가 있는 것이 Access Token임  
access_token = credentials.token
print(access_token)
