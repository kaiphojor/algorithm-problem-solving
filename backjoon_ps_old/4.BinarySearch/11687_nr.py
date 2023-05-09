#0912
from math import log
M = int(input())
"""
i = 0
five_count = 0

while five_count < M:
    i += 1
    n = 0
    f = i * 5
    while f % 5 == 0:
        f //= 5
        n += 1
    five_count += n
if five_count == M:
    print(i * 5)
else:
    print(-1)



def factorial_zero_count(z):
    i = 1 
    zero_count = 0
    while True:
        if (f:= i*5 )> z:
            break
        n = 0 
        while f != 1:
            f //= 5
            n +=1
        zero_count += n
        i += 1
    return zero_count
"""
s,e = 1, M 
V = 500000000
while s <= e:
    mid = (s + e) // 2
    zero_count = sum(map(lambda y: int(log(y,5)), filter(lambda x: x % 5 == 0,range(1,mid*5+1))))
    # zero_count = factorial_zero_count(mid * 5)
    if zero_count > M:
        e = mid-1
    elif zero_count <= M:
        s = mid+1
        if zero_count == M:
            V = min(V,mid * 5)
print(V if V != 500000000 else -1) 
