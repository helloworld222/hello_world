import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_04", GPIO.OUT)

while True:
    GPIO.output("P8_04", GPIO.HIGH)
    time.sleep(2)
    GPIO.output("P8_04", GPIO.LOW)
    time.sleep(2)

