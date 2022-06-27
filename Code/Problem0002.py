# Solution 1

import time
start_time = time.time()


def fibonacci(N):
    """Returns the Nth Fibonacci Number"""
    F = [0, 1] # Inital Fibonacci Numbers
    i = 0
    while i <= N-2:
        F_new = F[i] + F[i+1]
        F.append(F_new)
        i += 1
    return F[N]

N = 0 # Begin at the '0th' fibanacci number

even_fib_nums = []

while fibonacci(N) < 4000000:
    if round(fibonacci(N) / 2) == fibonacci(N) / 2:
        even_fib_nums.append(fibonacci(N))
    N += 1
 
print(sum(even_fib_nums))


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')

##############################################################################

# Solution 2

import time
start_time = time.time()


def fibonacci(N):
    """Returns the Nth Fibonacci Number"""
    F = [0, 1] # Inital Fibonacci Numbers
    i = 0
    while i <= N-2:
        F_new = F[i] + F[i+1]
        F.append(F_new)
        i += 1
    return F[N]

N = 0 # Begin at the '0th' fibanacci number

even_fib_sum = 0 # Starting sum 

while fibonacci(N) < 4000000:
    if round(fibonacci(N) / 2) == fibonacci(N) / 2:
        even_fib_sum += fibonacci(N)
    N += 1
    
print(even_fib_sum)


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')