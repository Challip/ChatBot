from tensorflow.keras.models import load_model
from collections import deque
import numpy as np
import cv2
import json
import cv2 as cv
import pickle


def video_class(path):
    
    modelA = load_model('../Assessment_AI_2022/PartC/modelA.h5')
    lb = pickle.loads(open("../Assessment_AI_2022/PartC/Coins_c/label.bin", "rb").read())
    with open('../Assessment_AI_2022/PartC/Coins_c/cat_to_name.json', 'r') as json_file:
        cat_2_name = json.load(json_file)

    mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
    Q = deque(maxlen=128)
    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print(" Exiting ...")
            break
        output = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224, 224)).astype("float32")
        frame -= mean
        nor_frame=frame/255
        aaaa=np.reshape(nor_frame,(1,1,nor_frame.shape[0],nor_frame.shape[1],nor_frame.shape[2]))
        preds=modelA.predict(aaaa)
        #preds=modelH.predict(np.expand_dims(nor_frame, axis=0))[0]
        Q.append(preds)
        results = np.array(Q).mean(axis=0)
        i = np.argmax(results)
        il = lb.classes_[i]
        pred=str(il)
        #label=pred
        label = cat_2_name[pred]
        text = "Prediction: {}".format(label)
        cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 225), 2)
        cv.imshow('frame',output)
        #print(preds)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

#video_class("C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/test_video/50p.MOV")