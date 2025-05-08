import RPi.GPIO as gpio
from time import sleep
import random
ledpin = (16,20,21)

gpio.setmode(gpio.BCM)
gpio.setup(ledpin, gpio.OUT)

try:
    while True :
        for pin in ledpin:
            gpio.output(pin, gpio.HIGH)
            sleep(0.05)
            gpio.output(pin, gpio.LOW)
            sleep(0.05)
            gpio.output(pin, gpio.HIGH)
            sleep(0.05)
            gpio.output(pin, gpio.LOW)
            sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()









