import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b);graph[b].append(a)

def dfs(root):
    stack = [root]
    visit = list()
    v_check = [0 for _ in range(N+1)]
    while stack:
        i = stack.pop()
        if v_check[i] == 0:
            visit.append(i)
            v_check[i] = 1
            stack.extend(sorted(graph[i],reverse=True))
    return visit

def bfs(root):
    visit = list()
    v_check = [0 for _ in range(N+1)]
    queue = deque([root])
    while queue:
        j = queue.popleft()
        if v_check[j] == 0:
            visit.append(j)
            v_check[j] = 1
            queue.extend(sorted(graph[j]))
    return visit
print(" ".join(map(str,dfs(V))))
print(" ".join(map(str,bfs(V))))