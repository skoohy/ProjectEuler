def max_prime_factor(N):
    max_factor = 0
    C = 2
    while N > 1:
        if N % C == 0:
            max_factor = N
            N = N / C
        else:
            C = C + 1
    return int(max_factor)

N = 600851475143 
print(max_prime_factor(N))
