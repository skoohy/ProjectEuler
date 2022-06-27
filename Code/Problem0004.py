import time
start_time = time.time()


x_y = [] 
max_palindrome = 0

for x in range(10, 1000):
    for y in range(10, 1000):
        number = x*y
        
        reversed_number = str(number)[::-1]
        reversed_number = int(reversed_number)
        
        if number == reversed_number and number > max_palindrome:
                max_palindrome = number
                x_y.append([x, y])
                
print(f'Largest palidrome {max_palindrome} found by multiplying {x_y[-1]}')


end_time = time.time()
print(f'Program Execution Time: {end_time-start_time} seconds')      