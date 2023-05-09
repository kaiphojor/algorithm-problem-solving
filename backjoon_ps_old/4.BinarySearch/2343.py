import sys
input = sys.stdin.readline
N, M = map(int,input().split())
video = list(map(int,input().split()))

s = max(video)
e = sum(video)
while s <= e:
    mid = (s + e ) // 2
    m = i = cur_sum = 0
    for i in range(N):
        if cur_sum + video[i] > mid:
            cur_sum = 0
            m += 1
        cur_sum += video[i]
    if cur_sum != 0:
        m += 1
    if m <= M:
        e = mid - 1
    else:
        s = mid + 1
print(s)