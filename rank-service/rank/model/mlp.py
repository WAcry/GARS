from tensorflow import keras

from rank.config import config


class RankModel:
    def __init__(self) -> None:
        self.model = keras.models.load_model(config['model_path'])

    # xs: list of features
    # [
    #   [A],
    #   [B],
    #   [C],
    # ]
    #
    # i.e.
    # [
    #   [[A cate features1], [A cate features2], [A num features]],
    #   [[B cate features1], [B cate features2], [B num features]],
    #   [[C cate features1], [C cate features2], [C num features]],
    # ]
    def predict(self, xs):
        return self.model.predict(xs)
