from utils.utils import brain
import cv2
import tensorflow as tf
import numpy as np

from utils.argparser import get_parser
from src.control import MovementControl
from src.control_test import TestMovementControl, TestMovementControl_1


if __name__ == '__main__':

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
        )
        
        ano = ''    
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, ai, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA)
            ## Change here for time between updates
            #if ct > 3 by default
            if ct > args["update_interval"]:
                
                #Connecting to servo and everything
                test_control = TestMovementControl_1()

                ai = brain(gray, x, y, w, h, f, i, o)
                ## Mechanical move here 
                if ai == "sadness":
                    test_control.Sadness()
                elif ai == "anger":
                    test_control.Anger()
                elif ai == "happy":
                    test_control.Happy()
                ct = 0

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


