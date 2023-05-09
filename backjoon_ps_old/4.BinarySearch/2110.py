# 입력을 받아서 정렬
N, C = map(int,input().split())
houses = sorted( int(input()) for _ in range(N))

# # 최대화 하고 싶은 대상 집 간 최소거리
# # 최소 거리 
s,e = 1,max(houses) - min(houses)
result = 0
while s <= e:
    mid = (s + e) // 2
    start = houses[0]
    counter = 1
    for i in range(1,N):
        if houses[i] - start >= mid:
            counter += 1 
            start = houses[i]
    if counter < C:
        e = mid - 1
    else:
        s = mid + 1
        result = max(result,mid)
print(result)