import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import pathlib
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from IPython.display import display
from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


while "models" in pathlib.Path.cwd().parts:
    os.chdir('..')
 
def load_model(model_name):
  base_url = 'http://download.tensorflow.org/models/object_detection/'
  model_file = model_name + '.tar.gz'
  model_dir = tf.keras.utils.get_file(
    fname=model_name, 
    origin=base_url + model_file,
    untar=True)
 
  model_dir = pathlib.Path(model_dir)/"saved_model"
  model = tf.saved_model.load(str(model_dir))
  return model
 
PATH_TO_LABELS = 'C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/Coins_c/object-detection.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

detection_model = tf.saved_model.load('C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/Coins_c/faster_rcnn_resnet50_coco_2017_11_08/saved_model/')
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/PartC/Coins_c/data/train_c')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR))

for image_path in TEST_IMAGE_PATHS:
    print(image_path)

file=[]
for dirname, _, filenames in os.walk(PATH_TO_TEST_IMAGES_DIR):
    for filename in filenames:
        file.append(os.path.join(dirname, filename))