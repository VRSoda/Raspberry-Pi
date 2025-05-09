import RPi.GPIO as gpio
from time import sleep
from threading import Thread

gpio.setmode(gpio.BCM)

LED_PINS = [16, 20, 21]
BUTTON_PINS = [13, 19, 26]

class Led:
    def __init__(self, pin):
        self.pin = pin
        gpio.setup(self.pin, gpio.OUT)
        gpio.output(self.pin, gpio.LOW)

    def set_state(self, state):
        gpio.output(self.pin, state)

    def on(self):
        self.set_state(gpio.HIGH)

    def off(self):
        self.set_state(gpio.LOW)

    def blink(self, duration=0.5):
        self.on()
        sleep(duration)
        self.off()
        sleep(duration)


class Button:
    def __init__(self, pin, button_number):
        self.pin = pin
        self.button_number = button_number
        self.prevState = gpio.LOW
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

    def wait_for_press(self):
        currentState = gpio.input(self.pin)
        if currentState == gpio.HIGH and self.prevState == gpio.LOW:
            Thread(target=handle_button_press, args=(self.button_number,)).start()
            sleep(0.3)
        self.prevState = currentState


leds = [Led(pin) for pin in LED_PINS]

def play_correct_password_pattern():
    print("비밀번호 성공")
    patterns = ["100", "010", "001"]
    for repeat in range(3):
        for pattern in patterns:
            for i, led in enumerate(leds):
                if pattern[i] == '1':
                    led.on()
                else:
                    led.off()
            sleep(0.8)

    for led in leds:
        led.off()


def play_incorrect_password_pattern():
    print("비밀번호 불일치")
    for repeat in range(3):
        for led in leds:
            led.on()
        sleep(0.5)
        for led in leds:
            led.off()
        sleep(0.5)

def handle_button_press(button_number):
    print(f"{button_number}번 버튼 클릭")
    if button_number == 1: leds[0].blink(0.1)
    elif button_number == 2: leds[1].blink(0.1)
    elif button_number == 3: leds[2].blink(0.1)
    sleep(0.5)

    if global_password == correct_password:
        print("비밀번호 일치")
        play_correct_password_pattern()
    else:
        print("비밀번호 실패")
        play_incorrect_password_pattern()


buttons = [
    Button(BUTTON_PINS[0], 1),
    Button(BUTTON_PINS[1], 2),
    Button(BUTTON_PINS[2], 3)
]

correct_password = "123"
global_password = ""

print("프로그램 시작")
try:
    global_password = input("비밀번호 입력 (111~333): ")
    print("1,2,3중 하나 버튼 클릭 : ")

    while True:
        for button in buttons:
            button.wait_for_press()
        sleep(0.01)

except KeyboardInterrupt:
    pass

finally:
    gpio.cleanup()
