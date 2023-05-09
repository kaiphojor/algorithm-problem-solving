N, M = map(int, input().split())
l = list( int(input()) for _ in range(N))

s,e = max(l),100000 * 100000 # 범위 중요
result = e
while s <= e:
    mid = (s + e ) // 2    
    wc = 1
    money = mid
    for m in l:
        if money < m:
            money = mid
            wc += 1
        money -= m

    if wc > M:
        s = mid + 1
    else:
        e = mid - 1
        result = min(result, mid)
print(result)
