import numpy as np
import matplotlib.pyplot as plt


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
    return
