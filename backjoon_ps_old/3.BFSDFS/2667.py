from collections import deque

def traverse(a,b):
    # queue 선언
    queue = deque()
    traverse_count = 0
    queue.append((a,b))
    while queue :
        i,j = queue.popleft()
        visited[i][j] = 1
        traverse_count += 1
        # queue에 넣기
        if i > 0:
            if n_list[i-1][j] == 1 and visited[i-1][j] == 0 and (i-1,j) not in queue:
                queue.append((i-1,j))
        if j > 0:
            if n_list[i][j-1] == 1 and visited[i][j-1] == 0 and (i,j-1) not in queue:
                queue.append((i,j-1))
        if i < N-1:
            if n_list[i+1][j] == 1 and visited[i+1][j] == 0 and (i+1,j) not in queue:
                queue.append((i+1,j))
        if j < N-1:
            if n_list[i][j+1] == 1 and visited[i][j+1] == 0 and (i,j+1) not in queue:
                queue.append((i,j+1))

    return traverse_count

N = int(input())
n_list = [list(map(int,input())) for _ in range(N)]
visited = [list([0]*N) for _ in range(N)]

apartment_list = []
for i in range(N):
    for j in range(N):
        if n_list[i][j] == 0:
            continue
        if visited[i][j] == 1:
            continue
        apartment_list.append(traverse(i,j))
print(len(apartment_list))
print(*sorted(apartment_list),sep="\n")