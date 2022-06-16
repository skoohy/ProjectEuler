import time
start_time = time.time()

x_y = []
max_palidrome = 0 
for x in range(10, 100):
    for y in range(10, 100):
        number = x*y
        reversed_number = str(number)[::-1]
        reversed_number = int(reversed_number)
        if number == reversed_number:
            if number > max_palidrome:
                max_palidrome = number
                x_y.append([x, y])
print(f'Largest palidrome {max_palidrome} found by multiplying {x_y[-1]}')
print("%s seconds" % (time.time() - start_time))


start_time = time.time()
x_y = []
max_palidrome = 0 
for x in range(100, 1000):
    for y in range(100, 1000):
        number = x*y
        reversed_number = str(number)[::-1]
        reversed_number = int(reversed_number)
        if number == reversed_number:
            if number > max_palidrome:
                max_palidrome = number
                x_y.append([x, y])
print(f'Largest palidrome {max_palidrome} found by multiplying {x_y[-1]}')
print("%s seconds" % (time.time() - start_time))



















  
            