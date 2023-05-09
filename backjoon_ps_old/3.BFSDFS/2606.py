#import sys
#sys.setrecursionlimit(10**6)
"""
n=int(input());m=int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b);g[b].append(a)
visit = [0]*(n+1)
def dfs(graph,root):
    visited = []
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph: 
                temp = list(set(graph[n])-set(visited))
                temp.sort()
                stack += temp
        print(visited)
        
    return " ".join(str(i) for i in visited)

print(dfs(g,1))
"""
"""
n=int(input()); m=int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b); g[b].append(a)
visit = [0]*(n+1)
def dfs(graph,s,visit):
    visit[s] = 1
    for i in graph[s]:
        if not visit[i]:
            dfs(graph,i,visit)
dfs(g,1,visit)
print(sum(visit)-1)
"""
# https://mingchin.tistory.com/214 답
"""
n = int(input()) 
m = int(input())
graph = [[] * n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0 
visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1 
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt += 1
dfs(1) 
print(cnt)
"""

"""
n = int(input())
c = int(input())
cl = list(list(map(int,input().split())) for _ in range(c))
d = dict()

for i, j in cl:
    if not d.get(i):
        d[i] = [j];        
    else:
        d[i] = d[i] + [j];
    if not d.get(j):
        d[j] = [i];        
    else:
        d[j] = d[j] + [i];
    
visited = list()
print(d)
def dfs(node, visited):
    visited.append(node)
    for e in d[node]:
        if e not in visited:
            dfs(e,visited)
dfs(1,visited)
print(len(visited)-1)
"""
n = int(input())
m = int(input())
visited = [0] * (n+1)
g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b);g[b].append(a)
def dfs(root):
    stack = [root]
    while stack :
        n = stack.pop()
        visited[n] = n
        stack += list(set(g[n]) - set(visited))
    print( len(list(i for i in visited if i != 0 and i != 1)))
dfs(1)
