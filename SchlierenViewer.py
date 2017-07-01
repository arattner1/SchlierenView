# Visualization software for the Schlieren imaging exhibit
#   At the Discovery Space of Central Pennsylvania
# Alex Rattner, 2017-07-01

import picamera
from PIL import Image
from time import sleep

c = picamera.PiCamera()

c.resolution = (1280, 720)
c.framerate = 24
c.start_preview()

sleep(10)


c.stop_preview()
