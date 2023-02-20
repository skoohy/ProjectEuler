counter_89 = 0

for num in range(1, 10000000):
    current_number = num
    while True:
        ss_digits = sum([int(a)**2 for a in str(current_number)])
        if ss_digits == 89:
            counter_89 += 1
            break
        elif ss_digits == 1:
            break
        current_number = ss_digits

print(counter_89)