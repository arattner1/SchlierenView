# Visualization software for the Schlieren imaging exhibit
#   At the Discovery Space of Central Pennsylvania
# Alex Rattner, 2017-07-01

import picamera
from time import sleep
import numpy as np


#Initialize camera
c = picamera.PiCamera()
wait(2)

#Get camera info (resolution)
resolution = c.resolution
W_cam = resolution[0]
H_cam = resolution[1]


#Try autocropping...
testframe = np.empty((W_cam, H_cam, 3), dtype=np.uint8)
c.capture(testframe, 'rgb')


# Wait indefinitely until the user terminates the script
#while True:
#    sleep(1)