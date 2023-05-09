
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
bridge = list(map(int,input().split()))
start, end = map(int,input().split())
queue = deque()
queue.append(start-1)
visited = [-1] * N
visited[start-1] = 0
end_flag = False
while queue:
    node = queue.popleft()
    for i,x in enumerate(bridge):
        if i == node:
            continue

        if (i-node) % bridge[node] == 0 and visited[i] == -1:
            visited[i] = visited[node] + 1
            queue.append(i)
            if i == end - 1:
                print(visited[i])
                end_flag = True
                break
    if end_flag:
        break
if visited[end -1] == -1:
    print(-1)



