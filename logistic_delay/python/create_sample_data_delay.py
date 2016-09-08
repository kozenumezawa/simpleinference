import numpy as np
import random
import csv
from math import floor

TIMESTEP = 25

tau = 10

b = 0
initial = random.random()
while(b < 0.9):
    divergence_flag = True
    while(divergence_flag):
        name = '../csv/inputdata_b_0_' + str(int(floor(b*10))) + '.csv'
        f = open(name, 'w')
        writer = csv.writer(f)

        X = []
        Y = []
        X.append(initial)
        Y.append(0)
        for t in range(1, TIMESTEP):
            x = X[t-1] * (3.5 - 3.5 * X[t-1])
            y = 0
            if(t > tau):
                y = b * X[t - tau]
            X.append(x)
            Y.append(y)
            if(X[t] > 10000 or X[t] < -10000):
                divergence_flag = True
        writer.writerows([X + Y])
        divergence_flag = False
        b += 0.1

#create noise data
name = '../csv/inputdata_noise.csv'
f = open(name, 'w')
writer = csv.writer(f)
X = []
Y = []
X.append(initial)
Y.append(0)
for t in range(1, TIMESTEP):
    x = X[t-1] * (3.5 - 3.5 * X[t-1])
    y = random.random()
    X.append(x)
    Y.append(y)
writer.writerows([X + Y])
