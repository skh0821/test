# Access Token 만드는 방법. 아래 라이브러리를 설치한 다음 사용할 것
# pip install --upgrade google-auth
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import random
import requests

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
# 서비스 계정으로 자격 증명 인증
credentials = service_account.Credentials.from_service_account_file(
    "smartfarm-f867f-firebase-adminsdk-4lk1a-0684caef8c.json", scopes=scopes)

# Use the credentials object to authenticate a Requests session.
# 자격 증명 개체를 사용하여 요청 세션을 인증합니다.
authed_session = AuthorizedSession(credentials)
response = authed_session.get(
    "https://smartfarm-f867f-default-rtdb.firebaseio.com/users/ada/name.json")


access_token = credentials.token
print(access_token)

# RTDB주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"

# 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
myobj = {'humi': random.randrange(0,100), 'temp': random.randrange(0, 50)}

# 아래는 RTDB의 쓰기 권한이 true일 때 사용
# requests.patch(url+"smartFarm.json", json = myobj).json()

# 아래는 RTDB의 쓰기 권한이 false일 때 사용, 위에서 만든 Access_token을 붙여서 데이터를 보냄
requests.patch(url+"smartFarm.json" + "?access_token=" + access_token, json = myobj).json()
