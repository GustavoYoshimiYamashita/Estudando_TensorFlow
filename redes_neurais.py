import numpy as np
import datetime
import tensorflow as tf

tf.keras.datasets.fashion_mnist.load_data()

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
