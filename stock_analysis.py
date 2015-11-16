import pandas as pd
import numpy as np

test=pd.read_csv("test.csv", header=0, \
                  delimiter=',', quoting=3, engine='python')

print("Hello WOrld")
counter=0

for i in range(test.shape[0]):
    

    row=test.iloc[i]

    for element in row:
        not_number=np.isnan(element)

        if not_number == True:
            counter=counter+1

    print(float(i)/test.shape[0])

print(float(counter)/test.shape[0]/test.shape[1])
