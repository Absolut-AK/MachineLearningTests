from tensorflow import keras
from tensorflow.python.keras.layers import Dense

model = keras.Sequential([Dense(units=1, input_shape=[3])])