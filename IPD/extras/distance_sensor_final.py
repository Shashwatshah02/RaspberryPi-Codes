import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(26,20)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    time.sleep(1)