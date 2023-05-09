def get_direction(d,x,y):
    nx,ny = x + dx[d], y + dy[d]
    is_change = False
    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        is_change = True
    elif matrix[nx][ny] == 1:
        is_change = True    
    if is_change:
        nx = x + dx[direction_change[d]]
        ny = y + dy[direction_change[d]]
        if matrix[nx][ny] == 0:
            return direction_change[d]
        else:
            return -1
    return d

M, N = map(int,input().split())
matrix = list(list(0 for _ in range(N)) for _ in range(M))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
direction_change = {0:3,1:2,2:0,3:1}
direction = 3
direction_change_count = 0
x,y = 0,0
while True:
    next_direction = get_direction(direction,x,y)
    if next_direction == -1:
        break
    elif direction != next_direction:
        direction_change_count += 1
    direction = next_direction
    matrix[x][y] = 1
    x = x + dx[direction]
    y = y + dy[direction]

print(direction_change_count)