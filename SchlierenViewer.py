# Visualization software for the Schlieren imaging exhibit
#   At the Discovery Space of Central Pennsylvania
# Alex Rattner, 2017-07-01

#Load in used modules
import picamera
from time import sleep
import numpy as np


#Initialize camera
c = picamera.PiCamera()
#Wait two seconds for camera to start-up
sleep(2)

#Set camera info (resolution)
W_cam = 1376
H_cam = 768
c.resolution = (W_cam,H_cam)


#Try autocropping...
#Get an image
testframe = np.empty((H_cam,W_cam,3), dtype=np.uint8)
c.capture(testframe, 'rgb')
#Sum to a brightness value
brightness = np.sum(testframe, axis=2)
#Find X-cm
colsum = np.sum(brightness, axis=0)
colsumthresh = 15000
colsum = (colsum>colsumthresh)*colsum
#Find Y-cm
rowsum = np.sum(brightness, axis=1)
rowsumthresh = 25000
rowsum = (rowsum>rowsumthresh)*rowsum
#Find spot size
xinds = np.arange(W_cam)
X_CM_Spot = np.sum(xinds*colsum)/np.sum(colsum)
W_Spot = 1.5*(np.where(colsum>0)[0][-1] - np.where(colsum>0)[0][0])
yinds = np.arange(H_cam)
Y_CM_Spot = np.sum(yinds*rowsum)/np.sum(rowsum)
H_Spot = 1.5*(np.where(rowsum>0)[0][-1] - np.where(rowsum>0)[0][0])


# Wait indefinitely until the user terminates the script
#while True:
#    sleep(1)