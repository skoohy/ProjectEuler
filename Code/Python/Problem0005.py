N = 1

while True:
    divisors_count  = 0
    for n in range(1,21):
        if N % n == 0:
            divisors_count += 1
        else:
            N += 1
            
    if divisors_count == 20:
        print(N)
        break    