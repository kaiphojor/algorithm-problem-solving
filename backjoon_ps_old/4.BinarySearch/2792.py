N, M = map(int,input().split())
gem = [ int(input()) for _ in range(M)]

print(gem)
l,r = 1,max(gem)
max_val = max(gem)
# for i in range(1,max(gem)+1):
while l <= r:
    i = ( l + r ) // 2
    # print("l r i maxval",l,r,i, max_val)
    member_count = N
    local_max = i
    for j,e in enumerate(gem):
        if member_count <= 0 or i >= e:
            local_max = max(local_max,e)
            member_count -= 1
        else:
            # print("i + left",i + e % i)
            local_max = max(local_max,i + e % i)
            member_count -= (e // i)
    if member_count < 0 :
        l = i + 1
    else:
        r = i - 1
        max_val = min(max_val, local_max)
    # member count <= 0 이면 share를 올린다
    # i >= e 되는 상황이 생기면 share를 내린다
print(max_val)

"""
import sys
input = sys.stdin.readline

def solve(lst, target):
    low, high = 1, max(lst)
    result, count = 0, 0
    while low <= high:
        count = 0
        mid = (low + high) // 2
        for i in lst:
            if i % mid == 0: count += (i // mid)
            else: count = count + (i // mid) + 1
        if count > target:
            low = mid + 1
        else:
            result = mid
            high = mid - 1

    return result
N, M = map(int, input().split())
color = []
for _ in range(M):
    color.append(int(input()))
print(solve(color, N))
"""
