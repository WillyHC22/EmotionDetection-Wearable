from skimage.transform import resize
import numpy as np
import cv2
import tensorflow as tf

def crop_center(img, x, y, w, h):    
    return img[y:y+h,x:x+w]

def preprocess_img(raw):
    img = resize(raw,(200,200, 3))
    img = np.expand_dims(img,axis=0)
    if(np.max(img)>1):
        img = img/255.0
    return img

def brain(raw, x, y, w, h, f, i, o):
    ano = ''
    img = crop_center(raw, x, y , w , h)
    img = preprocess_img(img)
    f.set_tensor(i['index'], img.astype(np.float32))
    f.invoke()
    res = f.get_tensor(o['index'])
    classes = np.argmax(res,axis=1)
    if classes == 0:
        ano = 'anger'
    elif classes == 1:
        ano = 'disgust'
    elif classes == 2:
        ano = 'fear'
    elif classes == 3:
        ano = "happy"
    elif classes == 4:
        ano = "neutral"
    elif classes == 5:
        ano = 'sadness'
    else :
        ano = 'surprised'
    return ano