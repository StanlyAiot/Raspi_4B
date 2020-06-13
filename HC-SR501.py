import RPi.GPIO as GPIO
import time

pinLED = 4 
pinSR = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinSR,GPIO.IN)

try:
    while True:
        if GPIO.input(pinSR):
            GPIO.output(pinLED, 1)
            print("dont move")
            time.sleep(0.1)
        else:
            GPIO.output(pinLED, 0)
            print("nobody here")
            time.sleep(0.1)
        
       
except KeyboardInterrupt:
    pass
GPIO.cleanup()




