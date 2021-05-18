from keras.models import model_from_json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import os
import numpy as np

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")

print('\n')


model.compile(  optimizer = 'adam',
                loss = 'sparse_categorical_crossentropy',
                metrics=['accuracy'])

valid = os.listdir("SmallTest/")

acc=0
i=0 # For checking if prediction is correct or not

# predicting
for fn in valid:

    path = 'SmallTest/' + fn + "/"
    l = os.listdir(path)[0]

    img = image.load_img(path+l, target_size=(300, 300))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    print(classes[0])
    if(i in np.where(classes==1.)):
        acc+=1
    i=i+1

print("\n\nCorrectly predicted:", 10*acc)