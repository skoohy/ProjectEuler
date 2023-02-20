import numpy as np

answer = 0
for n in range(1, 100000):
    if n != 1:
        if n != 2:
            if sum([np.math.factorial(int(a)) for a in str(n)]) == n:
                answer += sum([np.math.factorial(int(a)) for a in str(n)])
print(answer)
