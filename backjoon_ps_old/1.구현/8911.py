"""
영역 포함 하는 넓이 
0,0 -> 0,1 -> 0,2 -> turn left -> -1,2
영역별 좌표 저장
min max 구하기
차이 곱해서 영역 구하기
"""
dx,dy = [0,1,0,-1],[1,0,-1,0]

def move_dir(d, turn):
    if turn == 'L':
        d = (d - 1 if d > 0 else 3)
    elif turn == 'R':
        d = (d + 1 if d < 3 else 0)
    return d

T = int(input())
for _ in range(T):
    D = 0
    X,Y = [0],[0]
    loc = [0,0]
    for m in input().strip():
        l = 0
        if m in "LR":
            D = move_dir(D, m)
        elif m == 'F':
            l = 1
        elif m == 'B':
            l = -1

        x,y = loc[0] + dx[D] * l, loc[1] + dy[D] * l
        loc = [x,y]
        X.append(x)
        Y.append(y)
    L = R = F = B = 0

    L,R,F,B = min(X),max(X),max(Y),min(Y)
    print((R-L) * (F-B))

