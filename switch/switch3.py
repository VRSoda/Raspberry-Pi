import RPi.GPIO as gpio
from time import sleep

swPin = [13,19]
text = [
        "1번text",
        "2번text"
        ]
gpio.setmode(gpio.BCM)

for i in swPin:
    gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

def btncheck():
    for i in range(len(swPin)):
        pin = swPin[i]

        if gpio.input(pin) == gpio.HIGH:
            print(f"{i+1}버튼을 눌렀습니다")
            if i == 0:
                gpio.output(pin)
                print(text[0])
            elif i == 1:
                print(text[1])
            sleep(0.5)
            while gpio.input(pin) == gpio.HIGH:
    while True:
        btncheck()
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()
