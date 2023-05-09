from collections import deque
N = int(input())
queue = deque([1])
visited = set()
parent = [0] * (N+1)
t = {i:set() for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    t[a].add(b)
    t[b].add(a)
 
while queue:
    c = queue.popleft()
    s = t[c] - visited 
    for i in s:
        parent[i] = c
        queue.append(i)
    visited.add(c)
for p in parent[2:]:
    print(p)