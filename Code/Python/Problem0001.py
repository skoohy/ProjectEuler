N = 1000

threes   = range(3, N, 3)
fives    = range(5, N, 5)
fifteens = range(15, N, 15)

ans = sum(threes) + sum(fives) - sum(fifteens)

print(ans)

