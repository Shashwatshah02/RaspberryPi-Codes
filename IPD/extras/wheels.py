import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set up GPIO pins


GPIO.setup(7, GPIO.OUT)  # Connected to PWMA
GPIO.setup(11, GPIO.OUT)  # Connected to AIN2
GPIO.setup(12, GPIO.OUT)  # Connected to AIN1

GPIO.setup(15, GPIO.OUT)  # Connected to BIN1
GPIO.setup(16, GPIO.OUT)  # Connected to BIN2
GPIO.setup(18, GPIO.OUT)  # Connected to PWMB

print("Start")
GPIO.output(12, GPIO.LOW)
GPIO.output(11, GPIO.HIGH)
GPIO.output(7, GPIO.HIGH)

GPIO.output(16, GPIO.LOW)
GPIO.output(15, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
        
sleep(10000)
print("stop")        
GPIO.output(12, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(7, GPIO.LOW)

GPIO.output(16, GPIO.LOW) 
GPIO.output(15, GPIO.LOW) 
GPIO.output(18, GPIO.LOW) 








