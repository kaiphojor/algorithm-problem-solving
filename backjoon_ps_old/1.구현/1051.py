N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
cur = 0

for i in range(N):
    for j in range(M):
        l = len(arr)-i if len(arr)-i < len(arr[i])-j else len(arr[i])-j 
        for k in range(1,l):
            if arr[i][j] == arr[i][j+k]:
                if arr[i][j] == arr[i+k][j]:
                    if arr[i][j] == arr[i+k][j+k]:
                        cur = k if cur < k else cur
print((cur+1) ** 2)
