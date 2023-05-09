R, C, N = map(int, input().split())

# 2차원 행렬 입력 -> 
lattice = []
bombs = []
inversed_lattice = []
post_inversed_lattice = []
for i in range(R):
    lattice.append([])
    for j, e in enumerate(input().strip()):        
        if e == 'O':
            bombs.append([i, j])
        lattice[i].append(e)
    inversed_lattice.append(['O'] * C)
    post_inversed_lattice.append(['O'] * C)

dx,dy = [-1,1,0,0],[0,0,-1,1]
for bomb in bombs:
    x, y = bomb
    inversed_lattice[x][y] = '.'
    for n in range(4):
        nx,ny = x + dx[n], y + dy[n]
        if 0 <= nx < R and 0 <= ny < C:
            inversed_lattice[nx][ny] = '.'
# 전부 터트렸으면 
for i in range(R):
    for j in range(C):
        if inversed_lattice[i][j] == 'O':
            post_inversed_lattice[i][j] = '.'            
            for n in range(4):
                nx,ny = i + dx[n], j + dy[n]
                if 0 <= nx < R and 0 <= ny < C:
                    post_inversed_lattice[nx][ny] = '.'
# 0 초 - 폭탄 설치 (가운데) - 하나빼고다
# 1초 - 없음(가운데) - 하나빼고다
# 2초 - 나머지 설치(다) - 
# 3초 - 터지고 인접도 사라진다(꼭지점) - 아예 없음
# 4초 - 나머지에 설치(다) - 전부다
# 5초 - 터지고 인접이 사라진다(가운데) - 전부다
# 6초 - 나머지에 설치(다)
# 7초 - 터지고 인접도 사라진다(꼭지점) - 아예 없음
# 8초 - 나머지에 설치(다)
# 9초 - 터지고 인접이 사라진다(가운데)
# 1 + 4 * n (원래 입력)
# 3 + 4 * n (원래 입력 인접 터지고 남은 것)
def lattice_print(lattice):
    for row in lattice:
        print(''.join(row))
# 짝수면 그냥 출력
if N == 1:
    lattice_print(lattice)
if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
# 홀수중 원래 출력일 경우 
elif N % 4 == 1:
    lattice_print(post_inversed_lattice)
# 홀수 중 반전 출력일 경우
else:
    lattice_print(inversed_lattice)

