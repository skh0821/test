from machine import Pin, I2C
import network
import time
import urequests
import random

# 와이파이 정보 
SSID = 'U+Net03CC'
password = 'J6FDFE#490'

# 와이파이 연결하기
def wifiConnect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        # 와이파이 연결하기
        wlan.connect(SSID, password)  # 5, 6번 줄에 입력한 SSID와 password가 입력됨
        print("Waiting for Wi-Fi connection", end="...")
        print()
        while not wlan.isconnected():
            print(".", end="")
            time.sleep(1)
    else:
        print(wlan.ifconfig())
        print("WiFi is Connected")
        print()

# 와이파이 함수 실행
wifiConnect()

url = "파이어베이스 리얼타임 데이터베이스 주소"

# DB 내역 가져오기
response = urequests.get(url+".json").json()
print(response)
# print(response['smartFarm'])
# print(response['smartFarm']['led'])

while True:
    response = urequests.get(url+".json")
    response.close()
    # 객체 교체하기, 특정 주소의 데이터가 변경됨
    myobj = {'humi': random.randrange(0,100), 'temp': random.randrange(0, 50)}
    request = urequests.patch(url+"smartFarm.json", json = myobj)
    print(myobj)
    request.close()
    time.sleep(1)
