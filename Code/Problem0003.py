import time
start_time = time.time()

def prime_factorization(N):
    factors = []
    C = 2
    while N > 1:
        if N % C == 0:
            factors.append(C)
            N = N / C
        else:
            C = C + 1
    return factors

N = 600851475143 

print(max(prime_factorization(N)))

end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')

##############################################################################

import time
start_time = time.time()

def max_prime_factor(N):
    max_factor = 0
    C = 2
    while N > 1:
        if N % C == 0:
            max_factor = N
            N = N / C
        else:
            C = C + 1
    return max_factor

N = 600851475143 

print(max_prime_factor(N))

end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')