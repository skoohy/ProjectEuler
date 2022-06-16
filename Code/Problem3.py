import time
start_time = time.time()

def prime_factorization(n):
    factors = []
    c = 2
    while n > 1:
        if n % c == 0:
            factors.append(c)
            n = n / c
        else:
            c = c + 1
    return factors

n = 600851475143 

print(max(prime_factorization(n)))
print("%s seconds" % (time.time() - start_time))
