import RPi.GPIO as GPIO
from time import sleep

# setup GPIO
moistPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(moistPin, GPIO.IN)

while True:
    
    print('Moisture value: ', GPIO.input(moistPin))
    sleep(2)