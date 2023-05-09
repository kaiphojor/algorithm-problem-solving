import sys
input = sys.stdin.readline

# depth를 같이 넣어서 dfs 촌수 파악을 한다
def dfs(start,end):
    stack = [[start, 0]]
    visited = []
    while stack:
        element, depth = stack.pop()
        depth += 1
        for i in people_dict[element]:
            if i not in visited:
                if i == end:
                    return depth
                stack.append([i,depth])
        visited.append(element)
    return -1
n = int(input())
people_dict = {i:[] for i in range(1,n+1)}
a, b = map(int, input().split())
for _ in range(int(input())):
    x, y = map(int, input().split())
    people_dict[x].append(y)
    people_dict[y].append(x)
print(dfs(a, b))