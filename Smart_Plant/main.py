import RPi.GPIO as GPIO
from time import sleep

# setup GPIO
moistPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(moistPin, GPIO.IN)
pumpPin = 13
GPIO.setup(pumpPin, GPIO.OUT)


while True:
    state = GPIO.input(moistPin)
    print('State: ', state)
    if state == 0:
        GPIO.output(pumpPin, GPIO.LOW)
    elif state == 1:
        GPIO.output(pumpPin, GPIO.HIGH)
    state = not state
    sleep(2)