from functools import reduce
import sys
input = sys.stdin.readline
N, L, W, H = map(int, input().split())
low, high = 0, max(L,W,H)
for _ in range(100):
    mid = (low + high) / 2
    s = reduce(lambda a,b: a * b ,map(lambda a: a//mid,[L,W,H]))

    if s >= N:
        low = mid
    else:
        high = mid
print("%.10f"%(high))
        