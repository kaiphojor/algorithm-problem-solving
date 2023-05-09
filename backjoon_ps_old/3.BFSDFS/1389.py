"""
get min kevin bacon number 

케빈 베이컨 수 구하기

dict 구하기
케빈베이컨 수 리스트 초기화 [N+1] 
for 각 번호 에서 
	for i in range(상대방까지)
	    동일한 곳이라면 통과
		도달까지 while
            depth 추가
            
		min check
for 출력
"""
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
kevin_bacon_list = [0 for _ in range(N+1)]
minimum_value = 10000
relation = {n:set() for n in range(N+1)}
for i in range(M):
    a,b = map(int,input().split())
    relation[a].add(b)
    relation[b].add(a)

for n in range(1,N+1):
    kevin_bacon_num = 0
    for i in range(1,N+1):
        if n == i:
            continue
        depth = 1
        visited = set()
        connection = set([n])
        reached = False
        while depth < 100:
            visited = visited | connection
            buf = set()
            for c in connection:
                if i in relation[c]:
                    reached = True
                    break
                buf = buf | relation[c]
            if reached:
                break
            connection = buf - visited
            depth += 1
        kevin_bacon_num += depth
    kevin_bacon_list[n] = kevin_bacon_num
    minimum_value = min(minimum_value,kevin_bacon_num)

print(kevin_bacon_list.index(minimum_value))

"""
다른 사람의 잘 푼 풀이
https://chaewsscode.tistory.com/98

import sys
from collections import deque


def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    result = []
    for i in range(1, n+1):
        result.append(bfs(graph, i))

    print(result.index(min(result))+1)
"""