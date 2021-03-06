import time
start_time = time.time()


def sum_of_multiples(N):
    threes   = range(3, N, 3)
    fives    = range(5, N, 5)
    fifteens = range(15, N, 15)
    return sum(threes) + sum(fives) - sum(fifteens)

print(sum_of_multiples(1000))


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')
