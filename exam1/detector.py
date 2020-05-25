import os
import csv
import random
import shutil
import zipfile

import numpy as np
import matplotlib.pyplot as plt

from algorithm import Detector


def detect(path, detector):
    pred = []
    vals = []
    with open(path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            val = row.get('value')
            ret = detector.fit_predict(val)
            pred.append(float(ret))
            vals.append(float(val))
    return vals, pred


def plot(name, vals, pred):
    title = name.split('/')[1]

    anomaly_idx = np.where(np.array(pred) == 1)[0]
    anomaly_val = np.array(vals)[anomaly_idx]

    plt.figure(figsize=(10, 4))
    plt.title(title)
    plt.plot(vals)
    plt.scatter(anomaly_idx, anomaly_val, c='red', alpha=1, s=25, label='anomaly')
    plt.legend()
    plt.savefig(f'result/{title}.png')
    plt.close()


if __name__ == '__main__':

    if not os.path.exists('result'):
        os.mkdir('result')

    zip_path = 'data/time-series.zip'
    archive = zipfile.ZipFile(zip_path, 'r')

    for i in range(1, 68):
        detector = Detector()

        name = f'time-series/real_{i}.csv'
        path = archive.extract(member=name)

        vals, pred = detect(path, detector)
        plot(name, vals, pred)

    shutil.rmtree('time-series')
