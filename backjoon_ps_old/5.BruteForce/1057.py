N,k,l = map(int,input().split())
k,l = min(k,l),max(k,l)
round = 1

while N > 1:
    if k + 1 == l and l % 2 == 0 :
        break
    round += 1
    N = N//2 if N % 2 == 0 else N // 2 + 1
    k = k//2 + k % 2
    l = l//2 + l % 2

print(round)
