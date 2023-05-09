import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
R, C = map(int, input().split())
field = list(list(input().strip()) for _ in range(R))
wolf_count = sheep_count = 0
dx,dy = [-1,1,0,0],[0,0,-1,1]
area = []
def dfs(x,y):
    global area
    if x < 0 or x >= R or y < 0 or y >= C:
        return
    if (m := field[x][y]) == '#':
        return
    area.append(m)
    field[x][y] = '#'
    for i in range(4):
        dfs(x + dx[i],y + dy[i])
for r in range(R):
    for c in range(C):
        if field[r][c] != '#':
            area = []
            dfs(r,c)
            if (w := area.count('v')) < (s := area.count('k')):
                sheep_count += s
            else:
                wolf_count += w
print(sheep_count, wolf_count)