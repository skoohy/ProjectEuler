import numpy as np
import time as time
start_time = time.time()


max_side_lengths = 0
p = 120
while p <= 1000:
    
    side_lengths = []

    for a in range(1, 500):
        for b in range(a, 500):
            c = np.sqrt(a**2 + b**2)
            if a + b + c == p:
                side_lengths.append([a,b,c])

    if len(side_lengths) > max_side_lengths:
        max_side_lengths = len(side_lengths)
        print(f'Max Side Lengths = {max_side_lengths}, at a value p = {p}')             
    p = p + 1
    
    
end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')

##############################################################################

# Source: 
# https://radiusofcircle.blogspot.com/2016/05/problem-39-project-euler-solution
# -with-python.html
import numpy as np
import time
from collections import Counter

start_time = time.time()
p = 1000

perimeters = []

for a in range(1, 500):
    for b in range(a, 500):
        c = np.sqrt(a**2 + b**2)
        if int(c) == c and a + b + c <= p:
            perimeters.append(a+b+c)

p = Counter(perimeters)

print(p.most_common(1))

end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')