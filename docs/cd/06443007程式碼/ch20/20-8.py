from tensorflow.keras import models
from tensorflow.keras.layers import Dense

model = models.Sequential()
model.add(Dense(512, activation='relu', input_shape=(64,)))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', 
              metrics=['accuracy'])