import time
t1 = time.time()

powers = [a**b for a in range(2,101) for b in range(2,101)] # all terms
        
new = [] # new list containing distinct terms
for i in powers:
    if i not in new: # if i is not in new add it to new
        new.append(i)

print(len(new))

t2 = time.time()
print(t2-t1)

###############################################################################

import time
t1 = time.time()

print(len(set([a**b for a in range(2,101) for b in range(2,101)])))

t2 = time.time()
print(t2-t1)