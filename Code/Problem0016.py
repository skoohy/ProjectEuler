import time
start_time = time.time()

print(sum([int(a) for a in str(2**1000)]))

end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')