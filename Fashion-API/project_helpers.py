import tensorflow as tf
tf.__version__
from tensorflow.keras.datasets import fashion_mnist
from scipy.misc import imsave

# Load data from fashion_mnist dataset
(X_train, y_train),(X_test, y_test) = fashion_mnist.load_data()

for i in range(5):
    imsave(name="uploads/{}.png".format(i),
           arr=X_test[i])
