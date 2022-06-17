import time
start_time = time.time()

print(sum([int(a) for a in str(2**1000)]))

print("%s seconds" % (time.time() - start_time))