import sys
input = sys.stdin.readline
N = int(input())
min_comb = [i for i in range(N+1)]

s = 0
while True:
    sr = (s:=s+1) ** 2
    if sr > N:
        break
    min_comb[sr] = 1
for i in range(1,N+1):
    for j in range(1,i//2 + 1):
        min_comb[i] = min(min_comb[j]+min_comb[i-j],min_comb[i])
print(min_comb[N])