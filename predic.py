from keras.preprocessing.image import image
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model
import json
from PIL import Image



model = load_model('../Assessment_AI_2022/PartC/model.h5')
#map folder number to coin name
with open('../Assessment_AI_2022/PartC/Coins_c/cat_to_name.json', 'r') as json_file:
    cat_2_name_p = json.load(json_file)


def img_classi(target_path):  
    img=image.load_img(target_path,target_size=(224,224))
    X=image.img_to_array(img)/225
    input_arr=np.array([X])
    input_arr.shape
    pred= np.argmax(model.predict(input_arr))
    ii=str(pred)
    ans=cat_2_name_p[ii]
    ansText=("That coin is : " + ans)
    img = Image.open(target_path)
    fig = plt.figure(figsize=(224, 224))
    a=fig.add_subplot(len(target_path)/3,3,1)
    a.axis('off')
    imgplot = plt.imshow(img)
    a.set_title(ansText)
    plt.show()
   
    return ansText

#img_classi("C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/Coins_c/data/test_c/19/003__50 Pence_united_kingdom.jpg")
