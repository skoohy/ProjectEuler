max_palindrome = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        number = x*y
        
        reversed_number = str(number)[::-1]
        reversed_number = int(reversed_number)
        
        if number == reversed_number and number > max_palindrome:
                max_palindrome = number
            
print(max_palindrome)