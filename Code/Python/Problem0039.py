import numpy as np
from collections import Counter

p = 1000
perimeters  = []

for a in range(1, 500):
    for b in range(a, 500):
        c = np.sqrt(a**2 + b**2)
        if (a+b+c <= p) and (int(c) == c):
            perimeters.append(a+b+c)

occurences = Counter(perimeters)

print(int(occurences.most_common(1)[0][0]))
