import numpy as np
import random
import csv
from math import exp

f = open('../csv/input_transient_data.csv', 'w')
writer = csv.writer(f)

data = []
DATA_NUM = 10000
TIMESTEP = 100

R = 1
L = 10

data = []
for i in range(0, DATA_NUM):
    # Create one pair of time series data
    V = []
    I = []

    on_timing = random.randint(0,TIMESTEP-1)    # The timing when this switch is tunrned on.
    E = random.random()

    # Set initial values
    if(on_timing == 0):
        V.append(1)
    else:
        V.append(0)
    I.append(0)

    for t in range(1, TIMESTEP):
        v = 0
        i = 0
        if(t >= on_timing):
            v = E
            i = E / R * (1 - exp(- R / L * (t - on_timing)))

        V.append(v)
        I.append(i)
    writer.writerows([V])
    writer.writerows([I])
    data.append([V, I])

f.close()
npdata = np.array(data)
np.save('../npy/input_transient_data.npy', npdata)
