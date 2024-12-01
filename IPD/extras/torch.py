import RPi.GPIO as GPIO
import time

LED_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
        # Turn LED on
 # Wait for 1 second

except KeyboardInterrupt:
    GPIO.cleanup()  # Cleanup GPIO pins on Ctrl+C exit
