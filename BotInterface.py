import RPi.GPIO as GPIO
from time import sleep

# Servo PWM pin numbers
servo1 = 2 
servo2 = 3

# Setup the GPIO mode as BOARD so that you can reference the PINs on the board
GPIO.setmode(GPIO.BOARD)

# Set those pins to be voltage output
GPIO.setup(servo1, GPIO.OUT)
GPIO.setup(servo2, GPIO.OUT)

# Setup the frequency of the PWM signals 
# GPIO for PWM with 50Hz
s1 = GPIO.PWM(servo1, 50)
s2 = GPIO.PWM(servo2, 50) 

# set the initial position/angle of the servos
oldang1 = 0
oldang2 = 0
s1.start(oldang1) # Initialization
s2.start(oldang2)


def move(axis,angle): # Axis is "x","y","xy". Angle is from 0 - 180
    angle = angle / 18 + 2 # https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/ <-(explains it best)
    try:
        if(axis == "x"):
            s1.ChangeDutyCycle(angle) #  https://www.mbtechworks.com/projects/raspberry-pi-pwm.html
            sleep(0.5) #sleep for half a microsecond
        elif(axis == "y"):
            s2.ChangeDutyCycle(angle)
            sleep(0.5)
        elif(axis == "xy"):
            s1.ChangeDutyCycle(angle)  
            s2.ChangeDutyCycle(angle)
            sleep(0.5)
    except KeyboardInterrupt:
        s1.stop()
        s2.stop()
        GPIO.cleanup()


