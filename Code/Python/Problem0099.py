import numpy as np

data = np.loadtxt("./data/p099_base_exp.txt", delimiter=',') 

largest, max_index, count = 0, 0 , 1 

for x in data:
    value = x[1]*np.log(x[0])
    if value > largest: 
        largest = value 
        max_index = count 
    count += 1

print(max_index)