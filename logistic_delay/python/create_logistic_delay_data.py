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
        tau = random.randint(1,TIMESTEP)

        X = []
        Y = []
        X.append(random.random())
        Y.append(0)
        for t in range(1, TIMESTEP):
            x = X[t-1] * (3.5 - 3.5 * X[t-1])
            y = 0
            if(t > tau):
                y = X[t - tau]
            X.append(x)
            Y.append(y)
            if(X[t] > 10000 or X[t] < -10000):
                divergence_flag = True
    writer.writerows([X])
    writer.writerows([Y])
    writer2.writerows([X + Y])
    data.append([X, Y])

f.close()
npdata = np.array(data)
np.save('../npy/input_logistic_data.npy', npdata)
