import sys
input = sys.stdin.readline
N, L, W, H = map(int, input().split())
l,r = 0, max(L, W, H)

for _ in range(100):
    mid = (l + r ) / 2
    if N <= (L // mid) * (W // mid) * (H // mid):
        l = mid
    else:
        r = mid
print("%.10f"%(r))

