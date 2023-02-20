max_sum = 0

for a in range(1,100):
    for b in range(1,100):
            digit_sum = sum([int(a) for a in str(a**b)])
            if digit_sum > max_sum:
                max_sum = digit_sum

print(max_sum)
