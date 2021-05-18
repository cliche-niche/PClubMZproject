import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#For callbacks
class mcb(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
      if(logs.get('accuracy')>0.85):
        print("\nReached 85% accuracy so cancelling training!")
        self.model.stop_training = True
cb = mcb()



model = tf.keras.models.Sequential([
    # First convolution
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    
    # Second convolution
    tf.keras.layers.Conv2D(16, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # Wasn't used in the final training of the model
    # # Third convolution
    # tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    # tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(  optimizer = 'adam',
                loss = 'sparse_categorical_crossentropy',
                metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1/255)
valid_datagen = ImageDataGenerator(rescale=1/255)

train = train_datagen.flow_from_directory(
        'Trainimg/',
        target_size=(300, 300),
        batch_size=24,
        class_mode='sparse')

valid = valid_datagen.flow_from_directory(
        'Testimg/',
        target_size=(300, 300),
        batch_size=6,
        class_mode='sparse')

model.fit(
      train,
      steps_per_epoch=len(train),  
      epochs=15, # 15 epochs planned but exceeds 85% accuracy in just the second run
      verbose=1,
      validation_data = valid,
      callbacks=[cb])


# saving the model
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.h5")