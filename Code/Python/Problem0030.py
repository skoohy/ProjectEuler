import numpy as np

solution = 0 

for n in range(2, 354294):
    if sum( np.array([int(a) for a in str(n)])**5 ) == n :
                solution += n
                
print(solution)
