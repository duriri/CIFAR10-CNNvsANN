# -*- coding: utf-8 -*-
"""cfar10

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BIDaWE0LgPCVKyfiPmVLbCxGBxRvTGl3
"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

#Load the dataset
(X_train, y_train), (X_test,y_test) = datasets.cifar10.load_data()
X_train.shape

X_test.shape

X_test[1]
y_train[1]

y_train

X_train.shape

y_train.shape



y_train[:5]
print(type(y_train))

"""our y_train is 2D ,for our classification 1D array is better."""

y_train = y_train.reshape(-1,)

y_test = y_test.reshape(-1,)

# for show xlabel we need this list 
classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

"""plot some images to see what they are

"""

def plot_s(X, y, index):
    plt.figure(figsize = (15,2))
    plt.imshow(X[index])
    plt.xlabel(classes[y[index]])

plot_s(X_train, y_train, 551)

plot_s(X_train, y_train, 1)



"""##Normalizing the data"""

X_test[0]

X_train = X_train / 255.0
X_test = X_test/ 255.0

X_test[0]

"""***Build artificial neural network for image classification***


"""

ann = models.Sequential([
        layers.Flatten(input_shape=(32,32,3)),
        layers.Dense(3000, activation='relu'),
        layers.Dense(1000, activation='relu'),
        layers.Dense(10, activation='softmax')    
    ])

ann.compile(optimizer='SGD',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

ann.fit(X_train, y_train, epochs=1)

from sklearn.metrics import confusion_matrix , classification_report
import numpy as np
y_pred = ann.predict(X_test)
y_pred_classes = [np.argmax(element) for element in y_pred]

print("Classification Report: \n", classification_report(y_test, y_pred_classes))

"""## Now let us build a convolutional neural network to train our images"""

cnn = models.Sequential([
    #cnn
    layers.Conv2D(filters=26, kernel_size=(2, 2), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    #dense
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

cnn.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

cnn.fit(X_train, y_train, epochs=10)

cnn.evaluate(X_test,y_test)

y_pred = cnn.predict(X_test)
y_pred[:5]

y_classes = [np.argmax(element) for element in y_pred]
y_classes[:5]

y_test[:5]