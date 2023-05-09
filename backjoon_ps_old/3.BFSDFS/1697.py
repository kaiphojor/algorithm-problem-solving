import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())


def bfs():
    q = deque()             # deque는 양쪽에서 입출력 가능
    q.append(N)             # q = deque([5])
    while  q:
        x = q.popleft()     # 처음 시작점은 x = 5, q = deque([])
        if x == K:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):    # nx = 4, 6, 10
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)    # q = deque([4, 6, "10"])

MAX = 10 ** 5               # 시간초과 안나게 수 제한
dist = [0] * (MAX + 1)      # 이동하는 거리를 알기 위한 변수
# n, k = map(int, input().split())

bfs()

# ms = [ abs(N-i) for i in range(200001)]
# ms = [0] * 200001
# queue = deque()
# queue.append(N)
# while queue :
#     c = queue.popleft()
#     if c == K:
#         break
#     if 0 < c-1:
#         if ms[c-1] == 0:
#             queue.append(c-1)
#             ms[c-1] = ms[c]+1
#         else:
#             ms[c-1] = min(ms[c-1],ms[c]+1)
#     if c+1 < 100000:
#         if ms[c+1] == 0:
#             queue.append(c+1)
#             ms[c+1] = ms[c]+1
#         else:
#             ms[c+1] = min(ms[c+1],ms[c]+1)
#     if 0 < c * 2 < 200000:
#         if ms[c*2] == 0:
#             queue.append(c*2)
#             ms[c*2] = ms[c]+1
#         else:
#             ms[c*2] = min(ms[c*2],ms[c]+1)
# print(ms[K])

    


    # if 0 < c < 100000:
    #     ms[c*2] = min(ms[c]+1,ms[c*2])
    #     queue.append(c*2)
    # if 0 < c-1 <200000:
    #     ms[c-1] = min(ms[c-1],ms[c]+1)
    #     queue.append(c-1)
    # if 0 < c+1 < 200000:
    #     ms[c+1] = min(ms[c+1],ms[c]+1)
    #     queue.append(c+1)
    # if c == K:

def bfs(cur, dst, step):
    min_step = 1000
    queue = deque()
    queue.append((cur, step))
    while queue:
        c, s = queue.popleft()
        if c > 200000:
            continue
        if s > min_step:
            continue
        if c == dst:
            min_step = min(min_step,s)
            new_queue = deque()
            for t in queue:
                if t[1] < min_step:
                    new_queue.append(t)
            queue = new_queue
            continue
        if c < dst:
            queue.append((c+1,s+1))
            queue.append((c*2,s+1))
        queue.append((c-1,s+1))
    return min_step 
    
# print(bfs(N,K,0))