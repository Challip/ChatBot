# Importando as bibliotecas
import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import cv2
from keras.preprocessing.image import ImageDataGenerator, img_to_array, image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, GlobalAveragePooling2D
from keras.models import Model
file_path='C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/archive/coins/data'
data_train='C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/archive/coins/data/train'
data_valid='C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/archive/coins/data/validation'
data_test='C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/archive/coins/data/test'


#map folder number to coin name
with open('C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/archive/coins/data/cat_to_name.json', 'r') as json_file:
    cat_2_name = json.load(json_file)

# Listando 10 classes aleatórias
for i in np.random.choice(a = range(1,211), size = 10, replace=False):
    print('Classe '+str(i)+': '+cat_2_name[str(i)])
    
def load_image(file_path):
    return cv2.imread(file_path)


image_files = os.listdir(data_train)
train_images = [load_image(data_train) for file in image_files]

def preprocess_image(img, side=96):
    min_side = min(img.shape[0], img.shape[1])
    img = img[:min_side, :min_side]
    img = cv2.resize(img, (side,side))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img / 255.0

for i in range(len(train_images)):
    train_images[i] = preprocess_image(train_images[i])