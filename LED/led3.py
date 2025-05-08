import RPi.GPIO as gpio
from time import sleep
import random
lpin = 16
gpin = 20

gpio.setmode(gpio.BCM)
gpio.setup(lpin, gpio.OUT)
gpio.setup(gpin, gpio.OUT)

gpio.output(lpin, gpio.LOW)
gpio.output(gpin, gpio.LOW)
newpass = input("새로운 비밀번호 : ")
password = input("비밀번호 입력 : ")
if password != newpass:
    print("일치하지않")
    for _ in range(5):
        gpio.output(lpin, gpio.HIGH)
        sleep(0.1)
        gpio.output(lpin, gpio.LOW)
    else:
        print("설정완료")
while True:
    login = input("로그인비밀번호: ")
    if login == newpass:
        print("일치")
        gpio.output(gpin, gpio.HIGH)
        break
    else:
        print("불일치")
        for _ in range(5):
            gpio.output(lpin, gpio.HIGH)
            sleep(0.1)
            gpio.output(lpin, gpio.LOW)
            sleep(0.1)
