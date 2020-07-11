import tensorflow as tf


class Model:
    def __init__(self):
        mnist = tf.keras.datasets.mnist

        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        self.x_train, self.x_test = self.x_train / 255.0, self.x_test / 255.0

        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10)
        ])

        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

        self.model.compile(optimizer='adam',
                           loss=loss_fn,
                           metrics=['accuracy'])

    def fit(self, epochs):
        self.model.fit(self.x_train, self.y_train, epochs=epochs, verbose=2)

    def evaluate(self):
        self.model.evaluate(self.x_test, self.y_test, verbose=2)
