# 남의 풀이
from math import trunc
import sys
input = sys.stdin.readline
x, y = map(int, input().split())
e = trunc(100 * y / x)
low, high = 0, 1000000000
if e >= 99: 
    print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        tx, ty = x + mid, y + mid
        if trunc(100 * ty / tx) > e: 
            high = mid - 1
        else: 
            low = mid + 1
    print(high + 1)
"""   
시간초과 한 답         
from math import trunc
X, Y = map(int,input().split())
rate = trunc(Y/X * 100)
if X == Y:
    print(-1)
else:
    target_rate = rate + 1
    limit = 20000000
    right = limit
    left = 1
    while left <= right:
        mid = (left + right) // 2
        cur_rate = trunc((Y+mid) / (X+mid) * 100)
        next_rate = trunc((Y+mid+1) / (X+mid+1) * 100)
        print(mid,cur_rate,next_rate)
        print(left,right)
        if cur_rate != next_rate:
            if cur_rate == rate:
                mid += 1 
                break
            else:
                right = mid
        elif cur_rate > rate:
            right = mid
        else:
            left = mid
    print(mid)
"""
