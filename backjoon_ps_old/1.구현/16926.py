"""
돌리기
1초

돌리기
도는 주기
n = min(M,N) // 2
i = 0 - 0 ~ 11 - 12 (N+M) * 2 - 4
i = 1 - 0 ~ 3 - 4 (N+M) * 2 - 4 - 4  | (N+M)*2 -4 * (1 + i)
돌리기 - 어떻게 돌 것인가?
시작 -> 0 + i , 0 + i N-1+i 하, M-1+i 우, N-1+i 상, M-1+i 좌
출력하기

deque.rotate
규칙성 찾기

"""
import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
mat = list( list(map(int,input().split())) for _ in range(N))
nmat = list( [0 for _ in range(M)] for __ in range(N))

# 최소길이의 반절 만큼 테두리가 생긴다.
a = min(N,M) // 2
for b in range(a):
    temp = deque([])

    # 하단, 우측, 상단 좌측으로 이동하며 순회한다
    dx,dy = [1,0,-1,0],[0,1,0,-1]

    # 가로 세로는 점점 2 씩 줄어든다.
    x,y = N-1-2*b, M-1-2*b

    # 초기 위치
    i,j = 0+b, 0+b

    # 가로 세로 합 * 2 에 겹치는 꼭지점 제외. 테두리는 단계마다 8씩 줄어듬 
    r = (N+M) * 2 - 4 * (1 + b * 2)

    # 테두리 순회 할 때 1바퀴 이상을 돌지 않도록 설정
    nr = R % r
    
    # 테두리 순회하면서 값 가져와서 저장
    for k in range(x):
        print(i,j)
        temp.append(mat[i][j])
        i,j = i+dx[0],j+dy[0]
    for l in range(y):        
        print(i,j) 
        temp.append(mat[i][j])
        i,j = i+dx[1],j+dy[1]
    for k in range(x):
        print(i,j) 
        temp.append(mat[i][j])
        i,j = i+dx[2],j+dy[2]
    for l in range(y):        
        temp.append(mat[i][j])
        i,j = i+dx[3],j+dy[3]

    # 값 rotation
    temp.rotate(nr)

    # 새 배열에 rotation 적용한 값 집어넣기
    nn = 0
    i,j = 0+b, 0+b
    for k in range(x):
        nmat[i][j] = temp[nn]
        i,j = i+dx[0],j+dy[0]
        nn += 1
    for l in range(y):
        nmat[i][j] = temp[nn]
        i,j = i+dx[1],j+dy[1]
        nn += 1
    for k in range(x):
        nmat[i][j] = temp[nn]
        i,j = i+dx[2],j+dy[2]
        nn += 1
    for l in range(y):
        nmat[i][j] = temp[nn]
        i,j = i+dx[3],j+dy[3] 
        nn += 1

# 변환 배열 출력
for n in range(N):
    print(*nmat[n])