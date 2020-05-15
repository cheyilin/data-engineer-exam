# Data Engineer Exam

## 1. Anomaly Detecton

You have 67 time series data in `data/anomaly_detection/time-series.zip`, please add a columns called "anomaly".

Fill 1 if the point is anomaly else 0, you can use *any* method to detect anomaly.

( P.S. The time series data may contain 0 anomaly. )

## 2. Pandas

Please use [pandas](https://pandas.pydata.org/) transform `data/pandas/need_aggregate.csv` from Figure 1 to Figure 2.

+ Figure 1

![before](assets/before_aggregate.png)

+ Figure 2

![after](assets/after_aggregate.png)

## 3. Deep Learning

Use one of framework (*TensorFlow*/*PyTorch*/*Keras*) to build an LSTM Model, train and predict the file you produce on step 2.

Please point out which time point is an anomaly, Add a column called "anomaly", fill 1 if the point is anomaly else 0.
