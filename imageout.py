import cv2
import numpy as np
import os


cap = cv2.VideoCapture('06_intersection-over-union.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating data')

currentFrame = 0
while(True):

    ret, frame = cap.read()


    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1


cap.release()
cv2.destroyAllWindows()
