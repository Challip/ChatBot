
project_id = '39595fac-bdbc-42ea-bdb5-8deb64a4b14b'
cv_key = 'f636cbe46fc94797819e6e751b60f54f'
cv_endpoint = 'https://customvision10111.cognitiveservices.azure.com/'

model_name = 'coin'

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import matplotlib.pyplot as plt
from PIL import Image
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

credentials = ApiKeyCredentials(in_headers={"Prediction-key": cv_key})
custom_vision_client = CustomVisionPredictionClient(endpoint=cv_endpoint, credentials=credentials)

computervision_client = ComputerVisionClient(cv_endpoint, CognitiveServicesCredentials(cv_key))



def cloud_class(path):
    
    image_contents = open(path, "rb")
    classification = custom_vision_client.classify_image(project_id, model_name, image_contents.read())
    prediction = classification.predictions[0].tag_name
    img = Image.open(path)
    fig = plt.figure(figsize=(224, 224))
    a=fig.add_subplot(len(path)/3,3,1)
    a.axis('off')
    imgplot = plt.imshow(img)
    ans= ("Cloud prediction is : "+ prediction)
    a.set_title(ans)
    plt.show()
    return ans


