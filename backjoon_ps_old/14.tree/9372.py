import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    travel_graph = defaultdict(set)
    N, M = map(int, input().split())
    
    # 그래프 구성
    first = True    
    visited = set()
    queue = deque([])
    edge_count = 0

    for __ in range(M):
        a,b = map(int, input().split())
        if first:
            first = False
            queue.append(a)
            
        travel_graph[a].add(b)
        travel_graph[b].add(a)

    # 탐색, visited 
    while queue:
        loc = queue.popleft()
        if loc not in visited:
            edge_count += 1
            visited.add(loc)
            unvisited = travel_graph[loc] - visited
            for i in unvisited:
                if i not in queue:
                    queue.append(i)

    print(edge_count-1)
                