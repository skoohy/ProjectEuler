import time
t1 = time.time()

for a in range(1, 500):
    for b in range(a+1, 500):
        c = 1000 - b - a
        if a**2 + b**2 == c**2:
            print(a*b*c)
            print(f'Program Execution Time: {time.time()-t1} seconds')