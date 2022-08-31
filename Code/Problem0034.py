import time
t1 = time.time()


def fac(n):
    x = 1
    for ni in range(1, n+1):
        x = x * ni
    return x

answer = 0
for n in range(1, 100000):
    if n != 1:
        if n != 2:
            if sum([fac(int(a)) for a in str(n)]) == n:
                answer += sum([fac(int(a)) for a in str(n)])
print(answer)


t2 = time.time()
print(f'Program Execution Time: {t2-t1} seconds')