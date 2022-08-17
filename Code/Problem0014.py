import time
t1 = time.time()

largest_chain = 0
for n in range(2, 1000000):
    chain = [1]
    num = n # we save n here because inside the while loop, n will be reduced to 1
    while True:
        if n % 2 == 0: # is it even
            chain.append(n)
            n = n / 2
            
        elif n == 1: # our ending/breaking point, this is when we move to the next number in the for loop
            break
            
        else: # not even means its odd
            chain.append(n)
            n = 3*n + 1 
            
    if len(chain) > largest_chain: # compare chain length of current number
        largest_chain = len(chain)
        best_number = num
print(best_number)

t2 = time.time()
print(f'Program Execution Time: {t2-t1} seconds')