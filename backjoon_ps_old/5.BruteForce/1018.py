def get_minimum_coloring_count(arr,start_x,start_y):
    counter = 0
    for i in range(start_x,start_x+8):
        for j in range(start_y,start_y+8):
            if (i+j) % 2 == 0:
                if arr[i][j] == 'B':
                    counter += 1
            elif (i+j) % 2 == 1:
                if arr[i][j] == 'W':
                    counter += 1
    return counter if counter <= 32 else 64 - counter


N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]

min = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        cur = get_minimum_coloring_count(board,i,j)
        min = cur if cur < min else min
print(min)


