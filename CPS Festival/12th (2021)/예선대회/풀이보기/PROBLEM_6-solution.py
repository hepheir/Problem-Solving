from tensorflow.keras import layers, Sequential
import tensorflow as tf
import numpy as np


def make_model():
    model = Sequential([layers.Dense(1,
                                     activation='linear',
                                     input_shape=(1,))])
    optimizer = tf.optimizers.SGD(0.01)
    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mse'])
    return model


model = make_model()
model.summary()


train_x = [5, -15, 7, -7, -11, 3, -9, 1, -1, 11, 9, -13, 13, -3, -5]
train_y = [18, -82, 28, -42, -62, 8, -52, -2, -12, 48, 38, -72, 58, -22, -32]
predict_x = [11, -4, -9, 2, -10, -2, 0, -3, 1, -6, -7, -5, -8, -1]

model.fit(x=train_x,
          y=train_y,
          batch_size=16,
          epochs=256,
          shuffle=True)

predict_y = model.predict(x=predict_x)[:,0]

for x, y in zip(predict_x, predict_y):
    print(f'x: {x:<+4d},\ty: {round(y):<+4d} ({y:+f}),\tans: {5*x-7}')
