#test motion sensors
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from datetime import datetime
#from signal import pause
import RPi.GPIO as GPIO

# initialize

camera = PiCamera()

#filenameGlobal = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}".format(justnow)
#pir = MotionSensor(16)
#state = GPIO.input(16)


#private function
def start_camera(start):
    justnow = datetime.now()
    filenameGlobal = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}".format(justnow)
    if start =='ON' :
        camera.start_preview(alpha=50)
        camera.annotate_text = 'Motion deteched'
        camera.capture('/home/pi/Desktop/anuragimg/Motion%s.jpg' %filenameGlobal)
        sleep(2)
        camera.stop_preview()
    else:   
        camera.stop_preview()


#private function
def statistics(pir, state, motion):
    
    print(motion)
    print("pir active - %s" %pir.is_active)
    print("state - %s" %state)
    print("=======================================")
    
    


#action for 2

pir2 = MotionSensor(13)
state2 = GPIO.input(13)
print ('motion detection on Sensor2')
#pir2.wait_for_no_motion(timeout=5)

count=0

while True:
    sleep(1)
    count = count + 1
    if count ==10:
        break;
    print (count)
    
    if pir2.motion_detected :
        start_camera('ON')
        statistics(pir2, state2, 'Motion')
    else:
        statistics(pir2, state2, 'No Motion')




