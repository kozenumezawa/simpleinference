import numpy as np
import random
import csv
from math import floor

TIMESTEP = 25

initial = 0.1
b = 0
while(b < 0.9):
    divergence_flag = True
    while(divergence_flag):
        name = '../csv/inputdata_b_0_' + str(int(floor(b*10))) + '.csv'
        f = open(name, 'w')
        writer = csv.writer(f)
        divergence_flag = False

        X = []
        Y = []
        x_initial = random.random()
        y_initial = random.random()
        #X.append(x_initial)   #   initial value
        #Y.append(y_initial)   #   initial value
        X.append(initial)
        Y.append(initial)
        for t in range(1, TIMESTEP):
            X.append(X[t-1] * (3.8 - 3.8 * X[t-1] - 2 * b * Y[t-1]))
            Y.append(Y[t-1] * (3.5 - 3.5 * Y[t-1] - 0 * X[t-1]))
            if(X[t] > 10000 or X[t] < -10000):
                divergence_flag = True
        writer.writerows([X+Y])
        f.close()
    b = (floor(b * 10) + 1) / 10
