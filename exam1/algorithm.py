import random


class Detector:
    def fit_predict(self, ptr):
        pred = random.choices([0, 1], weights=[0.99, 0.01])[0]
        return pred
