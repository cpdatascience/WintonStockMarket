import pandas as pd
import numpy as np
import random
import sys

test=pd.read_csv("test.csv", header=0, \
                 delimiter=',', quoting=3, engine='python')

counter_A=0
data= []

for i in range(test.shape[0]):
    counter_B=0
    #counter_A+= 1

    row=test.iloc[i]

    for element in row:
        rnd = random.random()
        if rnd <= .1:
            data.append([element, counter_A, counter_B])
            element = 0
        counter_B+= 1
    counter_A+= 1

f = open("data.txt", "a");
for item in data:
    f.write('\n'.join(str(item)))

f.close()
