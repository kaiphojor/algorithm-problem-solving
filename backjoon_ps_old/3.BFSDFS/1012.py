import sys
input = sys.stdin.readline
dx,dy = (-1,1,0,0),(0,0,-1,1)

def is_adjacent(loc, li):
    for l in li:
        for c in range(4):
            if l[0] + dx[c] == loc[0] and l[1] + dy[c] == loc[1]:
                return True
    return False
T = int(input())

result = []
for _ in range(T):
    M, N, K = map(int,input().split())
    cabbage_connection = []
    for _ in range(K):
        x,y = map(int,input().split())
        is_added = False
        for conn in cabbage_connection:
            if is_adjacent((x,y),conn):
                is_added = True
                conn.append((x,y))
                break
        if not is_added:
            cabbage_connection.append([(x,y)])

    i = 0
    while i < len(cabbage_connection):
        merge_index = []
        for j in range(i+1,len(cabbage_connection)):
            for c in cabbage_connection[j]:
                if is_adjacent(c,cabbage_connection[i]):
                    merge_index.append(j)
                    break
        changed = False 
        for r in reversed(merge_index):
            changed = True
            cabbage_connection[i].extend(cabbage_connection.pop(r))
        if not changed:
            i += 1
    result.append(len(cabbage_connection))

for r in result:
    print(r)
"""
bfs 사용한 풀이
https://pacific-ocean.tistory.com/270
t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
                s[q][w] = 0
                queue.append([q, w])
for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            if s[q][w] == 1:
                bfs(q, w)
                s[q][w] = 0
                cnt += 1
    print(cnt)

"""