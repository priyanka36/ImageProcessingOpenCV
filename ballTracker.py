from collections import deque
from imutils.video import VideoStream
import numpy as np 
import argparse 
import cv2 
import imutils 
import time 

ap = argparse.ArgumentParser()
ap.add_argument("-v","--video")
ap.add_argument("-b","--buffer")
args = vars(ap.parse_args())