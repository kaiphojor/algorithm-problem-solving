import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
D = list(map(int, input().split()))
V = list ( list( False for _ in range(M+1)) for __ in range(N+1))
V[0][S] = True
result = -1
for i,diff in enumerate(D):
    for j in range(M+1):
        if V[i][j]:
            if j-diff >= 0:
                V[i+1][j-diff] = True
            if j+diff <= M:
                V[i+1][j+diff] = True
for i in range(M,-1,-1):
    if V[N][i] == True:
        result = i
        break
print(result)