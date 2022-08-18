import time
t1 = time.time()

counter_89 = 0 
for num in range(1, int(10e6)+1):
    current_number = num
    while True:
        ss_digits = sum([int(a)**2 for a in str(current_number)]) # sum_square_digits

        if ss_digits == 89:
            counter_89 += 1
            break
        elif ss_digits == 1: # We don't need to do anything when we get a 1 other than end the loop and move on
            break 
        current_number = ss_digits
        
print(counter_89)

t2 = time.time()
print(f'Program Execution Time: {t2-t1} seconds')