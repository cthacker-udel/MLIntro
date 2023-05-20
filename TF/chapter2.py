import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import tensorflow.keras as keras

data = tf.keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) = data.load_data()

training_images = training_images / 255.0
test_images = test_images / 255.0

# First layer is the 28x28 grid of the image Second layer a randomly chosen number, very high and possibility of
# over-fitting, very low and possibility of under-fitting
model = keras.models.Sequential(
    [keras.layers.Flatten(input_shape=(28, 28)), keras.layers.Dense(128, activation=tf.nn.relu),
     (keras.layers.Dense(10, activation=tf.nn.softmax))])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)

model.evalutate(test_images, test_labels)
