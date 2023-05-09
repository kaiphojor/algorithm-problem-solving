"""
시간 초과 한 내답변
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
trust_dict = {n: set() for n in range(1, N+1)}
len_dict = {n:[] for n in range(100001)}
max_val = 0
result = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    trust_dict[b].add(a)

for num in range(1, N+1):
    stack = []
    stack.append(num)
    visited = set()
    while stack: 
        n = stack.pop()
        trusted = trust_dict[n]
        stack.extend(trusted - visited)
        # for j in trusted:
        #     if j not in visited:
        #         stack.append(j)
        visited.add(n)
    pc_count = len(visited)-1
    max_val = max(pc_count, max_val)
    len_dict[pc_count].append(num)

print(*len_dict[max_val])
# print(*[i for i in range(1, N+1) if result[i] == max_val], sep=" ")


for num in range(1, N+1):
    queue = deque()
    queue.append(num)
    visited = set()
    while queue: 
        n = queue.popleft()
        trusted = trust_dict[n]
        queue.extend(trusted - visited)
        # for j in trusted:
        #     if j not in visited:
        #         queue.append(j)
        visited.add(n)
    pc_count = len(visited)-1
    max_val = max(pc_count, max_val)
    len_dict[pc_count].append(num)

"""

"""
출처: https://cotak.tistory.com/130 [TaxFree]

"""
import sys
import collections
def bfs(start):
    cnt = 1 
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = collections.deque([start])
    while queue:
        u = queue.popleft()
        for v in g[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1
                cnt += 1
    return cnt                 
n, m = map(int, sys.stdin.readline().split())
g = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[b].append(a)
results = []
max_cnt = 0
for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    results.append([i, cnt])
for i, cnt in results:
    if cnt == max_cnt:
        print(i, end = ' ')

