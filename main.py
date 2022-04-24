import tensorflow as tf
import numpy as np

# Criando uma constante
tensor = tf.constant([[1, 2], [3, 4]])
tensor_2 = tf.constant([[5, 6], [7, 8]])

print(tensor.shape)

# Operações com as constantes
# Somando
print(tensor + 2)
# Multiplicando
print(tensor * 5)
# Elevando ao quadrado
print(np.square(tensor))
# Raiz quadrada
print(np.sqrt(tensor))
# Produto escalar
print(np.dot(tensor, tensor_2))