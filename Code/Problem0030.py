import numpy as np
import time
start_time = time.time()


solution = 0 
for n in range(2, 1000000):
    if sum( np.array([int(a) for a in str(n)])**5 ) == n :
                solution = solution + n
print(solution)


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')

##############################################################################

import numpy as np
import time
start_time = time.time()


solution = 0 
for n in range(2, 354294):
    if sum( np.array([int(a) for a in str(n)])**5 ) == n :
                solution = solution + n
print(solution)


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')