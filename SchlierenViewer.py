# Visualization software for the Schlieren imaging exhibit
#   At the Discovery Space of Central Pennsylvania
# Alex Rattner, 2017-07-01

import picamera
from time import sleep
import numpy as np


#Initialize camera
c = picamera.PiCamera()
sleep(2)

#Set camera info (resolution)
W_cam = 1376
H_cam = 768
c.resolution = (W_cam,H_cam)


#Try autocropping...
testframe = np.empty((H_cam,W_cam,3), dtype=np.uint8)
c.capture(testframe, 'rgb')
brightness = np.sum(testframe, axis=2)
colsum = np.sum(brightness, axis=0)
colsumthresh = 15000
colsum = (colsum>colsumthresh)*colsum
xinds = np.arange(W_cam)
np.sum(xinds*colsum)/np.sum(colsum)




# Wait indefinitely until the user terminates the script
#while True:
#    sleep(1)