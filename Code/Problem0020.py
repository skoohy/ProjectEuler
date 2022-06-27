import time
import numpy as np
start_time = time.time()


print(sum([int(a) for a in str(np.math.factorial(100))]))


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')

##############################################################################

import time
import math as m
start_time = time.time()


print(sum([int(a) for a in str(m.factorial(100))]))


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')

##############################################################################

import time
start_time = time.time()


def factorial(n):
    """Returns the factorial of n, for n >= 0"""
    result = 1
    for ni in range(2, n+1):
        result = result * ni
    return result

print(sum([int(a) for a in str(factorial(100))]))


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')