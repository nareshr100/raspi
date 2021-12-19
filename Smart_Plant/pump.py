import RPi.GPIO as GPIO
from time import sleep

# setup GPIO
pumpPin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pumpPin, GPIO.OUT)

state = False
while True:
    print('State: ', state)
    if state == 0:
        GPIO.output(pumpPin, GPIO.LOW)
    elif state == 1:
        GPIO.output(pumpPin, GPIO.HIGH)
    state = not state
    sleep(2)