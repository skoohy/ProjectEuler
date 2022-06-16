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

fib_even_sum = 0 # Starting sum 

while fibonacci(N) < 4000000:
    if round(fibonacci(N) / 2) == fibonacci(N) / 2:
        fib_even_sum += fibonacci(N)
    N += 1
    
print(fib_even_sum)
print("%s seconds" % (time.time() - start_time))
