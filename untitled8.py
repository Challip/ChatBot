

from datetime import timedelta
import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
from keras.preprocessing.image import image
from keras.preprocessing.image import ImageDataGenerator, img_to_array
import matplotlib.pyplot as plt

modelH = load_model('C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/modelH.h5')
path="C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/Video1.mp4"
cap = cv2.VideoCapture(path)
count=0

success=1
while success:
    success, frame = cap.read()
    target_path='C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/frame0.jpg'
    img=image.load_img(target_path,target_size=(224,224))
    plt.imshow(frame)
    X=image.img_to_array(img)/225
    input_arr=np.array([X])
    input_arr.shape
    
    pred= np.argmax(modelH.predict(input_arr))
    pred=str(pred)
    print (pred)
    count += 1
    cv2.destroyAllWindows()
