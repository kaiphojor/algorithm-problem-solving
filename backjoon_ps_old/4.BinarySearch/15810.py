#15810
N, M = map(int, input().split())
t = list(map(int, input().split()))
s, e = 0, M * max(t)
min_value = max(t) * M
while s <= e:
    mid = (s + e) // 2
    # 해당 시간에 만든 풍선 갯수
    val = 0
    for i in t:
        val += (mid // i)
    if val >= M:
        min_value = min(min_value, mid)
        e = mid - 1
    else:
        s = mid + 1    
print(min_value)
