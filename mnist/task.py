from .model import Model


def train_and_evaluate():
    model = Model()

    model.fit(5)

    model.evaluate()


if __name__ == '__main__':
    train_and_evaluate()
