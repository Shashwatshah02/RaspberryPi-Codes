import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import dht11
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import DistanceSensor
    
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT)  # Connected to PWMA
GPIO.setup(11, GPIO.OUT)  # Connected to AIN2
GPIO.setup(12, GPIO.OUT)  # Connected to AIN1

GPIO.setup(15, GPIO.OUT)  # Connected to BIN1
GPIO.setup(16, GPIO.OUT)  # Connected to BIN2
GPIO.setup(18, GPIO.OUT)  # Connected to PWMB

instance = dht11.DHT11(pin=21) # temperature & humidity
sensor = DistanceSensor(26,20) # Distance sensor

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

database = firestore.client()
collection = database.collection("wheels")



while True:
    controller = collection.document('controller').get().to_dict()
    if sensor.distance < 0.06:
        print('Danger Ahead !!!', sensor.distance, 'm')
        GPIO.output(12, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(16, GPIO.LOW) 
        GPIO.output(15, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW)
        collection.document('distance').set({'dist':sensor.distance})
        sleep(1)
        continue
    if controller['forward'] == True:
        GPIO.output(12, GPIO.LOW)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
    elif controller['left'] == True:
        GPIO.output(12, GPIO.LOW)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
    elif controller['right'] == True:
        GPIO.output(16, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
    elif controller['behind'] == True: 
        GPIO.output(12, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(16, GPIO.LOW) 
        GPIO.output(15, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW)
        break









print(controller['forward'])


controller = collection.document('controller').get().to_dict()

print(controller['forward'])


    


# set up GPIO pins




