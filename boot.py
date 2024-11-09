from machine import Pin
from utime import sleep

# 전원이 들어온지에 대한 모니터링용 코드
led = Pin(27, Pin.OUT)

led.on()
sleep(0.2)
led.off()
sleep(0.2)
led.on()
sleep(0.2)
led.off()
sleep(0.2)
led.on()
sleep(0.2)
led.off()
sleep(0.2)

# main.py 파일 임포트
import main
