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


N, x = 0, 1000 

while len(str(fib(N))) <= x:
    if len(str(fib(N))) == x:
        print(N)
        break     
    N = N + 1
