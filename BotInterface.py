# sudo blkid  //to find the drive name
# sudo mount (drive location) (where to[file locatioin])      ex: sudo mount /dev/sda1 /mnt
# sudo unmount (file location)  ex: sudo unmount /mnt
import RPi.GPIO as GPIO
from time import sleep
import sys

# Servo PWM pin numbers
servo1 = 17
servo2 = 27

# Setup the GPIO mode as BCM so that you can reference the PINs on the board
GPIO.setmode(GPIO.BCM)

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
angle = 0
cal = False



def Calibrat():
    # 45 <-> 135
    print("Calibration starting!")
    print("Angle : 45")
    move("xy", 45)
    sleep(0.8)
    print("Angle : 90")
    move("xy", 90)
    sleep(0.8)
    print("Angle : 135")
    move("xy", 135)
    sleep(0.8)
    move("xy", 90)
    sleep(0.8)
    cal = True
    print("Done!")


def move(axis, ang):  # Axis is "x","y","xy". Angle is from 0 - 180
    if(cal == True):
        angle = angle + (ang / 18 + 2) # https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/ <-(explains it best)
    else:
        angle = ang / 18 + 2
    print(axis,ang)
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
    s1.stop()
    s2.stop()
    GPIO.cleanup()



