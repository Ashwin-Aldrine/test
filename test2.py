from picamera2 import Picamera2
from time import sleep
camera=Picamera2()
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture_file('/home/ashwin/Desktop/image%s.jpg'%i)
camera.stop_preview()