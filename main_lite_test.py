from skimage.transform import resize
import cv2
import tensorflow as tf
import numpy as np

from utils.argparser import get_parser
from utils.utils import brain
from control import MovementControl
import RPi.GPIO as GPIO
import time

args = get_parser()

print('Loading ..')

f = tf.lite.Interpreter("/home/pi/Desktop/CAFA_Wearable/models/model_optimized.tflite")
f.allocate_tensors()
i = f.get_input_details()[0]
o = f.get_output_details()[0]

print('Load Success !')

cascPath = "/home/pi/Desktop/CAFA_Wearable/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)


cap = cv2.VideoCapture(-1)
ai = 'anger'
img = np.zeros((200, 200, 3))
ct = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ct+=1
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(150, 150)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    
    ano = ''    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, ai, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA)
        ## Change here for time between updates
        #if ct > 3
        if ct > args["update_interval"]:

            #print('Connecting to servo...')
            control = MovementControl(args)

            ai = brain(gray, x, y, w, h)
            ## Mechanical move here 
            if ai == "sadness":
                control.Sadness()
            elif ai == "anger":
                control.Anger()
            elif ai == "happy":
                control.Happy()
            ct = 0

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


