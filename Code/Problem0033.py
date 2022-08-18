import numpy as np
from fractions import Fraction
import time as time
t1 = time.time()

numbers = []
count = 0

for x in range(10, 100):
    for y in range(10, 100):
        if x / y < 1:
            x_digits = [int(a) for a in str(x)]
            y_digits = [int(a) for a in str(y)]
            for x_dig in x_digits:
                for y_dig in y_digits:
                    if x_dig != 0: 
                        if y_dig != 0:
                            if x_dig == y_dig:
                                x_digits.remove(x_dig) 
                                y_digits.remove(y_dig)
                                new_x = x_digits[0]
                                new_y = y_digits[0]
                                if new_x and new_y != 0:
                                    if x/y == new_x / new_y:
                                        numbers.append(new_x / new_y)
                                        count += 1
                                    
product = np.prod(numbers)
solution = Fraction(product).limit_denominator()
print(solution)
print(count)

t2 = time.time()
print(f'Program Execution Time: {t2-t1} seconds')
