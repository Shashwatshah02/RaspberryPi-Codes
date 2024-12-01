from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(26,20)

while True:
    
    sleep(1)
    if sensor.distance < 0.1:
        print("Danger")
        print('Distance to nearest object is', sensor.distance, 'm')