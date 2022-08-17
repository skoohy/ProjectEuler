import time
t1 = time.time()

max_sum = 0
for a in range(1,100):
    for b in range(1,100):
            digit_sum = sum([int(a) for a in str(a**b)])
            if digit_sum > max_sum:
                max_sum = digit_sum

print(max_sum)

t2 = time.time()
print(f'Program Execution Time: {t2-t1} seconds')

##############################################################################

import time
t1 = time.time()

digit_sums = []
for a in range(1,100):
    for b in range(1,100):
            digits = [int(a) for a in str(a**b)]
            digit_sums.append(sum(digits))

print(max(digit_sums))

t2 = time.time()
print(f'Program Execution Time: {t2-t1} seconds')