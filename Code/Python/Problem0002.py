def fib(N):
    F_n, F_n1 = 0, 1
    i = 0
    
    if N == 0:
        return F_n
    elif N == 1:
        return F_n1
    
    while i <= N-2:
        F_new = F_n + F_n1
        F_n, F_n1 = F_n1, F_new
        i += 1
        
    return F_new    
    
N = 0
even_fibonacci_sum = 0 

while fib(N) < 4e6:
    if fib(N) % 2 == 0:
        even_fibonacci_sum += fib(N)
    N += 1

print(even_fibonacci_sum)


