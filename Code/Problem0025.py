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

N = 0 # Starting with the '0'-th fibonacci number
x = 1000 # We want the first fibonacci number that has 1000 digits

while len(str(fibonacci(N))) <= x: # Run loop until a fibonacci number is found with 1000 digits
    if len(str(fibonacci(N))) == x:
        print(N)
        break     
    N = N + 1

    
end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')