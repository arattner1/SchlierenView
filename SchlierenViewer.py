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
X_CM_Spot = np.sum(xinds*colsum)/(np.sum(colsum)+1)
W_Spot = 1.5*(np.where(colsum>0)[0][-1] - np.where(colsum>0)[0][0])
yinds = np.arange(H_cam)
Y_CM_Spot = np.sum(yinds*rowsum)/(np.sum(rowsum)+1)
H_Spot = 1.5*(np.where(rowsum>0)[0][-1] - np.where(rowsum>0)[0][0])
S_spot = max(W_Spot, H_spot)

#Convert spot into camera units (0-1)
x_cam_spot = (X_CM_Spot-S_Spot/2.0)/W_cam
y_cam_spot = (Y_CM_Spot-S_Spot/2.0)/H_cam
w_cam_spot = S_Spot/W_cam
h_cam_spot = S_Spot/H_cam

if (x_cam_spot + w_cam_spot/2.0) > 1.0:
	x_cam_spot = 1.0 - w_cam_spot
if (y_cam_spot + h_cam_spot/2.0) > 1.0:
	y_cam_spot = 1.0 - h_cam_spot


#Camera display
c.zoom = (x_cam_spot,0.0, w_cam_spot,1.0)  
c.start_preview()
sleep(10)
c.stop_preview()
c.close()


# Wait indefinitely until the user terminates the script
#while True:
#    sleep(1)