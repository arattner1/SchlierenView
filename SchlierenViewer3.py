# Visualization software for the Schlieren imaging exhibit
#   At the Discovery Space of Central Pennsylvania
# Alex Rattner, 2017-09-26

#Load in used modules
import picamera
from time import sleep
import numpy as np
from datetime import datetime as dt
import pickle
import os.path
from Getch import _Getch

#Bounding camera window:
def BoundWindow(x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot):
    w_cam_spot = max(min(1.0, w_cam_spot), 0.05)
    x_cam_spot = min(max(x_cam_spot,0), 1.0 - w_cam_spot)
    h_cam_spot = max(min(1.0, h_cam_spot), 0.05)
    y_cam_spot = min(max(y_cam_spot,0), 1.0 - h_cam_spot)
    return (x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot)
    


#Setup to read in individual chars
GetChar = _Getch()

#Initialize camera
c = picamera.PiCamera()
#Wait two seconds for camera to start-up
sleep(2)

#Set camera info (resolution)
W_cam = 1376
H_cam = 768
c.resolution = (W_cam,H_cam)


#Final camera settings
c.sharpness = 50
c.brightness = 70
c.saturation = 30
c.video_stabilization = False


#Initialize camera positions:
x_cam_spot = 0 
w_cam_spot = 1
y_cam_spot = 0 
h_cam_spot = 1

#Load positions from file (if available)
if os.path.isfile("Positions.p"):
    (x_cam_spot,y_cam_spot,w_cam_spot,h_cam_spot) = pickle.load( open("Positions.p", "rb") )

c.rotation = 90

#Camera display
c.zoom = (x_cam_spot,y_cam_spot, w_cam_spot,h_cam_spot)  
c.start_preview()

#At this point either save a picture or exit
while True:
    inp = GetChar()
    
    #print(inp)

    #Zoom in
    if inp == "=": 
        x_cam_spot = x_cam_spot + 0.025*w_cam_spot
        w_cam_spot = 0.95*w_cam_spot
        y_cam_spot = y_cam_spot + 0.025*h_cam_spot
        h_cam_spot = 0.95*h_cam_spot
        (x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot) = BoundWindow(x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot)
        #print(x_cam_spot, ", ", y_cam_spot, ", ", w_cam_spot, ", ", h_cam_spot)
        pickle.dump( (x_cam_spot,y_cam_spot,w_cam_spot,h_cam_spot), open("Positions.p", "wb") )
        c.zoom = (x_cam_spot,y_cam_spot, w_cam_spot,h_cam_spot)  
    #Zoom in
    elif inp == "-":
        w_cam_spot = (1.0/0.95)*w_cam_spot
        x_cam_spot = x_cam_spot - 0.025*w_cam_spot
        h_cam_spot = (1.0/0.95)*h_cam_spot
        y_cam_spot = y_cam_spot - 0.025*h_cam_spot
        (x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot) = BoundWindow(x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot)
        #print(x_cam_spot, ", ", y_cam_spot, ", ", w_cam_spot, ", ", h_cam_spot)
        pickle.dump( (x_cam_spot,y_cam_spot,w_cam_spot,h_cam_spot), open("Positions.p", "wb") )
        c.zoom = (x_cam_spot,y_cam_spot, w_cam_spot,h_cam_spot)  
    #Go left
    elif inp == "a":
        x_cam_spot = x_cam_spot + 0.025*w_cam_spot
        (x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot) = BoundWindow(x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot)
        #print(x_cam_spot, ", ", y_cam_spot, ", ", w_cam_spot, ", ", h_cam_spot)
        pickle.dump( (x_cam_spot,y_cam_spot,w_cam_spot,h_cam_spot), open("Positions.p", "wb") )
        c.zoom = (x_cam_spot,y_cam_spot, w_cam_spot,h_cam_spot)
    #Go right
    elif inp == "d":
        x_cam_spot = x_cam_spot - 0.025*w_cam_spot
        (x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot) = BoundWindow(x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot)
        #print(x_cam_spot, ", ", y_cam_spot, ", ", w_cam_spot, ", ", h_cam_spot)
        pickle.dump( (x_cam_spot,y_cam_spot,w_cam_spot,h_cam_spot), open("Positions.p", "wb") )
        c.zoom = (x_cam_spot,y_cam_spot, w_cam_spot,h_cam_spot)
    #Go up
    elif inp == "s":
        y_cam_spot = y_cam_spot + 0.025*h_cam_spot
        (x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot) = BoundWindow(x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot)
        #print(x_cam_spot, ", ", y_cam_spot, ", ", w_cam_spot, ", ", h_cam_spot)
        pickle.dump( (x_cam_spot,y_cam_spot,w_cam_spot,h_cam_spot), open("Positions.p", "wb") )
        c.zoom = (x_cam_spot,y_cam_spot, w_cam_spot,h_cam_spot)
    #Go down
    elif inp == "w":
        y_cam_spot = y_cam_spot - 0.025*h_cam_spot
        (x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot) = BoundWindow(x_cam_spot, y_cam_spot, w_cam_spot, h_cam_spot)
        #print(x_cam_spot, ", ", y_cam_spot, ", ", w_cam_spot, ", ", h_cam_spot)
        pickle.dump( (x_cam_spot,y_cam_spot,w_cam_spot,h_cam_spot), open("Positions.p", "wb") )
        c.zoom = (x_cam_spot,y_cam_spot, w_cam_spot,h_cam_spot)  

    elif inp == "S":
        filename = "/home/pi/Pictures/" + str(dt.now()) + ".jpg"
        c.capture(filename, use_video_port=True)
    elif inp == "x":
        break


#End routine
c.stop_preview()
c.close()

