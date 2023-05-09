import sys
input = sys.stdin.readline

dx,dy = [-1,0,1,0],[0,1,0,-1]
d_dict = {0:"위",1:"오른쪽",2:"아래",3:"왼쪽"}
N, M = map(int,input().split())
A, B, d = map(int,input().split())
g_map = [list(map(int,input().split())) for _ in range(N)]
"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
visited = 1
g_map[A][B] = 2 
is_stop = False
while not is_stop:
    ori_d = d
    for i in range(4):
        d = 3 if d == 0 else d - 1
        if  0 <= dx[d] + A < N and 0 <= dy[d] + B < M:
            new_A = dx[d] + A
            new_B = dy[d] + B        
            if g_map[new_A][new_B] == 0:
                visited += 1
                A, B = new_A, new_B
                g_map[A][B] = 2
                break
        if i == 3:
            if 0 <= -dx[d] + A < N and 0 <= -dy[d] + B < M:
                new_A = -dx[d] + A
                new_B = -dy[d] + B        
                if g_map[new_A][new_B] == 0:               
                    g_map[new_A][new_B] = 2
                    visited += 1
                    A, B = new_A, new_B
                    break
            is_stop = True
print(visited)