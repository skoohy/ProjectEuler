largest_chain = 0

for n in range(2, 1000000):
    chain_count = 0
    current_number = n
    while True:
        if n % 2 == 0: 
            chain_count += 1
            n = n / 2
            
        elif n == 1: 
            break
            
        else: 
            chain_count += 1
            n = 3*n + 1 
            
    if chain_count > largest_chain: 
        largest_chain = chain_count
        best_number = current_number
        
print(best_number)