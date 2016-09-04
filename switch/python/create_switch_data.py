import numpy as np
import random
import csv

f = open('../csv/input_switch_data.csv', 'w')
writer = csv.writer(f)

data = []
DATA_NUM = 10000
TIMESTEP = 100

data = []
for i in range(0, DATA_NUM):
    # Create one pair of time series data
    X = []
    Y = []

    on_timing = random.randint(0,TIMESTEP-1)    # The timing when this switch is tunrned on.

    # Set initial values
    if(on_timing == 0):
        X.append(1)
    else:
        X.append(0)
    Y.append(0)

    for t in range(1, TIMESTEP):
        x = 0
        y = 0
        if(t == on_timing):
            x = 1
        if(t == on_timing + 1):
            x = 1
            y = 1
        if(Y[t-1] == 1):
            y = 1

        X.append(x)
        Y.append(y)
    writer.writerows([X])
    writer.writerows([Y])
    data.append([X, Y])

f.close()
npdata = np.array(data)
np.save('../npy/input_switch_data.npy', npdata)
