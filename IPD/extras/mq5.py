import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(23,24)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configure GPIO pins
GPIO.setup(14, GPIO.IN)   
GPIO.setup(12, GPIO.OUT) 
GPIO.output(12, False)   

while True:
    gas_sensor_state = GPIO.input(12)
    
    if gas_sensor_state == False:  
        while GPIO.input(14) == True:
            GPIO.output(12, True)
            print("Gas Leakage Detected!")
            print('Distance to nearest object is', sensor.distance, 'm')
        
    else:
        GPIO.output(12, False)
        print("Not Detected!")