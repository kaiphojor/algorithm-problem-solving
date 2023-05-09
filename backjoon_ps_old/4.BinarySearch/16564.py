"""
팀내 최소레벨 = T 
최소레벨의 최대화
조정 -> 최소레벨
할당 레벨양 K
K >= sum (최소레벨 - 현재 레벨 ) 
    레벨 = max(레벨, 현재레벨)
    최소레벨 높이기
else:
    최소레벨 다운 

"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
levels = list( int(input()) for _ in range(N))
s,e = min(levels), 10 ** 9

result_level = 0
while s <= e:
    mid = (s + e ) // 2 

    required = 0
    for l in levels:
        if l < mid:
            required += (mid - l)

    if K >= required:
        result_level = max(result_level, mid)
        s = mid + 1 
    else:
        e = mid - 1

print(result_level)
