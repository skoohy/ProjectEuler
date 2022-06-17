import time
import numpy as np
start_time = time.time()

print(sum([int(a) for a in str(np.math.factorial(100))]))

print("%s seconds" % (time.time() - start_time))