import numpy as np
import random

data = []
for i in range(0, 10):
    #   Create one pair of time series data by using Logistic Equation
    divergence_flag = True
    while(divergence_flag):
        divergence_flag = False
        b = random.random()
        
        X = []
        Y = []
        X.append(random.random())   #   initial value
        Y.append(random.random())   #   initial value
        for t in range(1, 100):
            X.append(X[t-1] * (3.8 - 3.8 * X[t-1] - b * Y[t-1]))
            Y.append(Y[t-1] * (3.5 - 3.5 * Y[t-1] - 0.1 * X[t-1]))
            if(X[t] > 10000):
                divergence_flag = True

    data.append([X, Y])

npdata = np.array(data)
np.save('logistic.npy', npdata)
