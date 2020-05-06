import tensorflow as tf
import keras
import matplotlib.pyplot as plt
import numpy as np

from keras.preprocessing import image

img_array = np.empty((20, 256*256*3))

for i in range (20):
    x=image.img_to_array(image.load_img(("img_train/img{}.png").format(i), target_size=(256,256)))
    x = np.reshape(x, (256*256*3))
    img_array[i,:] = x
    
centroide = np.mean(img_array, axis=0)
centroide = np.reshape(centroide, (256,256,3))/255
plt.imshow(centroide)