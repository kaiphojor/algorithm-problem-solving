import sys
input = sys.stdin.readline
N, K = map(int, input().split())
calc_count = 0
while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    calc_count += 1
print(calc_count)