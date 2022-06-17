import time
start_time = time.time()

for a in range(1, 500):
    for b in range(a+1, 500):
        c = 1000 - b - a
        if a**2 + b**2 == c**2:
            print(a,b,c)
            print(a*b*c)
            print("%s seconds" % (time.time() - start_time))