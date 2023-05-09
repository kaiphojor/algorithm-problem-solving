from math import trunc
import sys
input = sys.stdin.readline
X, Y = map(int, input().split())
Z = trunc(Y * 100 / X )

l, r = 1, X
result = -1
if Z < 99:
    while l <= r :
        mid = (l + r) // 2
        if Z < trunc(100 * (Y+mid) / (X+mid) ):
            r = mid - 1
        else:
            l = mid + 1
    result = r + 1
print(result)