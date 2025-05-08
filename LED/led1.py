import RPi.GPIO as gpio
from time import sleep

ledpin = (16,20,21)

# BCM = GPIO 핀번호
# BOARD = 해당하는 보드 번호

gpio.setmode(gpio.BCM)
gpio.setup(ledpin, gpio.OUT)

try:
    while True:
        number = int(input("mode(1:lpin, 2:gin, 3:ypin : "))
        mode = input("mode on off : ")
        if mode == "on":
            gpio.output(ledpin[number - 1], gpio.HIGH)
        elif mode == "off":
            gpio.output(ledpin[number - 1], gpio.LOW)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()




