import scipy

count = 0

for r in range(1, 101):
    for n in range(r, 101):
        if scipy.special.comb(n,r) > 1e6:
            count += 1

print(count)