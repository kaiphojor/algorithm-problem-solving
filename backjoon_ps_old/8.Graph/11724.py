N,M = map(int,input().split())
set_list = list()
for _ in range(M):
    u,v = map(int,input().split())
    cur_set = set([u,v])
    is_found = False
    for s in set_list:
        if u in s or v in s:
            s = s | cur_set
            is_found = True
            break
    if not is_found:
        set_list.append(cur_set)
print(len(set_list))
"""
dfs, 인접리스트 사용한 타인의 답
import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)
            
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
"""