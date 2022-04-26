import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras

from keras.preprocessing.image import ImageDataGenerator, img_to_array, image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, GlobalAveragePooling2D
from keras.models import Model
dataset='../input/coin-images/coins/data'

data_train='C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/Coins_c/data/train_c'
data_valid='C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/Coins_c/data/validation_c'
data_test='C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/archive/coins/data/test'

#map folder number to coin name
with open('C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/Coins_c/cat_to_name.json', 'r') as json_file:
    cat_2_name1= json.load(json_file)

print(cat_2_name1['17'])

batch_size=60

# Transforms
datagen_train = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.1,  # randomly shift images horizontally 
    height_shift_range=0.1,  # randomly shift images vertically
    horizontal_flip=True,
    featurewise_std_normalization=True, # Normalize images
    samplewise_std_normalization=True)

datagen_valid = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.1,  # randomly shift images horizontally
    height_shift_range=0.1,  # randomly shift images vertically
    horizontal_flip=True,
    featurewise_std_normalization=True,
    samplewise_std_normalization=True)

datagen_test = ImageDataGenerator(
    rescale=1./255,
    featurewise_std_normalization=True,
    samplewise_std_normalization=True)

train_generator = datagen_train.flow_from_directory(
        data_train,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical')

valid_generator = datagen_valid.flow_from_directory(
        data_valid,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical')

test_generator = datagen_test.flow_from_directory(
        data_test,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical')


import matplotlib.pyplot as plt


# Lets have a look at some of our images
images, labels = train_generator.next()

fig = plt.figure(figsize=(20,10))
fig.subplots_adjust(wspace=0.2, hspace=0.4)

# Lets show the first 32 images of a batch
#for i, img in enumerate(images[:32]):
 #   ax = fig.add_subplot(4, 8, i + 1, xticks=[], yticks=[])
  #  ax.imshow(img)
   # image_idx = np.argmax(labels[i])
    
    
    
    
int_to_dir = {v: k for k, v in train_generator.class_indices.items()}

## Build the model
output_classes = 100

model = keras.Sequential(
    [
        keras.Input(shape=(28,28,1)),
        keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        keras.layers.MaxPooling2D(pool_size=(2, 2)),
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        keras.layers.MaxPooling2D(pool_size=(2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(256, activation="relu"),
        keras.layers.Dense(100, activation="sigmoid"),
    ]
)
# compile the model (should be done *after* setting layers to non-trainable)
model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


num_train = len(train_generator.filenames)
num_valid = len(valid_generator.filenames)
num_test = len(train_generator.filenames)

model.fit(train_generator,steps_per_epoch=num_train//batch_size, epochs=10)
## Evaluate the trained model
score = model.evaluate_generator(test_generator, steps=num_test//1, verbose=1)
print('\n', 'Test accuracy:', score[1])