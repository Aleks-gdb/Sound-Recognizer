import joblib
import numpy as np
from PIL import Image

CATEGORIES = ["Flute", "Guitar", "Saxophone", "Trumpet", "Tuba", "Violin"]

def preprocess(img):
  pil_im = Image.open(img)
  gray_im = pil_im.convert('LA')
  std_size = (360, 1440)
  gray_im = gray_im.resize(std_size)
  img_arr = np.array(gray_im)
  img_arr = np.reshape(img_arr, [360,1440,2])
  img_arr = np.true_divide(img_arr, 255.0)
  return img_arr[:,:,[0]]

def evaluateGraph(img):
  #prepares the image to be used by the model
  img_arr = preprocess(img)
  img_arr = np.array(img_arr).reshape((1,360,1440,1))



  #load the trained model
  #ADD FULL FILE PATH
  loaded_model = joblib.load('finalized_model(3).sav') #ADD FULL FILE PATH
  #ADD FULL FILE PATH


  
  #tests the model against an individual graph
  scores = loaded_model.predict(img_arr)
  max = 0

  print(scores)

  for i in range(len(scores[0])):
    if(scores[0][i]>max):
      max = scores[0][i]
      label = CATEGORIES[i]

  #outputs the determined label
  return label
