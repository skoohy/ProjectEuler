import numpy as np
import time
t1 = time.time()

data = np.loadtxt("./data/p099_base_exp.txt", delimiter=',') # load data

largest, max_index, count = 0, 0 , 1 # largest pair found, index of that largest pair, keep count of all index

for x in data: # x  will be an array such as [632382 518061]
    value = x[1]*np.log(x[0])
    if value > largest: # compare value with the previous value
        largest = value # save current largest value pair
        max_index = count # save the index at which the largest pair was found
    count += 1

print(max_index)

t2 = time.time()
print(f'Program Execution Time: {t2-t1} seconds')