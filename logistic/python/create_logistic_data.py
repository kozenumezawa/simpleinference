import numpy as np
import random
import csv
from math import exp

f = open('../csv/input_logistic_data.csv', 'w')
f2 = open('../csv/input_logistic_data_connect.csv', 'w')
writer = csv.writer(f)
writer2 = csv.writer(f2)

data = []
DATA_NUM = 5000
TIMESTEP = 25
for i in range(0, DATA_NUM):
    #   Create one pair of time series data by using Logistic Equation
    divergence_flag = True
    while(divergence_flag):
        divergence_flag = False
        b = random.random()

        X = []
        Y = []
        X.append(random.random())   #   initial value
        Y.append(random.random())   #   initial value
        for t in range(1, TIMESTEP):
            X.append(X[t-1] * (3.8 - 3.8 * X[t-1] - b * Y[t-1]))
            Y.append(Y[t-1] * (3.5 - 3.5 * Y[t-1] - 0 * X[t-1]))
            if(X[t] > 10000 or X[t] < -10000):
                divergence_flag = True
    writer.writerows([X])
    writer.writerows([Y])
    writer2.writerows([X + Y])
    data.append([X, Y])

f.close()
npdata = np.array(data)
np.save('../npy/input_logistic_data.npy', npdata)
