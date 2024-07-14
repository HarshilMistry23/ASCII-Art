import cv2 as cv
import numpy as np
import itertools
#ASCII Characters to be there in the sketch
ASCII_CHARS = [".",",",":","!","|","I","C","S","A","R","T"]
img = cv.imread('Path to image.jpg')
def rescaleFrame(frame,scale1,scale2):
    global width 
    width = int(frame.shape[1] * scale1)
    height = int(frame.shape[0] * scale2)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

#scale the frame as required
pic = rescaleFrame(img,0.1600009,0.120095)     #115 and 130
#pic = rescaleFrame(img,0.0330687831,0.0297619048)   #100 and 120

gray = cv.cvtColor(pic,cv.COLOR_BGR2GRAY)
cv.namedWindow('grayed', cv.WINDOW_NORMAL)
cv.imshow('grayed',gray)
cv.resizeWindow('grayed', 3024,4032)
flat_list = list(itertools.chain(*gray))   #to make a single list from nested lists

characters = "".join([ASCII_CHARS[pixel//25] for pixel in flat_list])
asciiimg = "\n".join([characters[index:(index+ width)] for index in range(0, len(characters), width)])
print(asciiimg)
print(len(characters))
print(width)
cv.waitKey(0)
    




