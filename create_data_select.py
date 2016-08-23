import numpy as np
import random
import csv

# 同じ初期値で、bによって挙動がどう変わるかを調べたいので、
# 初期値は同じ値を用いる
divergence_flag = True
while(divergence_flag):
    f = open('./csv/inputdata_b_low.csv', 'w')
    writer = csv.writer(f)
    divergence_flag = False
    b = 0
    X = []
    Y = []
    x_initial = random.random()
    y_initial = random.random()
    X.append(x_initial)   #   initial value
    Y.append(y_initial)   #   initial value
    for t in range(1, 100):
        X.append(X[t-1] * (3.8 - 3.8 * X[t-1] - b * Y[t-1]))
        Y.append(Y[t-1] * (3.5 - 3.5 * Y[t-1] - 0.1 * X[t-1]))
        if(X[t] > 10000 or X[t] < -10000):
            divergence_flag = True
    writer.writerows([X])
    writer.writerows([Y])
    f.close()

    f = open('./csv/inputdata_b_high.csv', 'w')
    writer = csv.writer(f)
    b = 0.95
    X = []
    Y = []
    X.append(x_initial)   #   initial value
    Y.append(y_initial)   #   initial value
    for t in range(1, 100):
        X.append(X[t-1] * (3.8 - 3.8 * X[t-1] - b * Y[t-1]))
        Y.append(Y[t-1] * (3.5 - 3.5 * Y[t-1] - 0.1 * X[t-1]))
        if(X[t] > 10000 or X[t] < -10000):
            divergence_flag = True
    writer.writerows([X])
    writer.writerows([Y])
    f.close()
