import time
start_time = time.time()

Sum_Squares = 0
S = 0

for i in range(1, 101):
    Sum_Squares += (i)**2
    S += i
    
Square_Sum = (S)**2

print(Square_Sum - Sum_Squares)
print("%s seconds" % (time.time() - start_time))
