
import RPi.GPIO as GPIO

pinLED = 21 
freq = 0.5
dc = 50 

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED,GPIO.OUT)
p = GPIO.PWM(pinLED, freq)

p.start(dc)
input(" press Enter to stop")
p.stop()
GPIO.cleaup()


# test agin..........

