sum_of_squares = 0
s = 0

for i in range(1, 101):
    sum_of_squares += (i)**2
    s += i
    
square_of_sum = (s)**2

print(square_of_sum - sum_of_squares)