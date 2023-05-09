import sys
input = sys.stdin.readline

dx,dy = [-1,1,0,0],[0,0,-1,1]
move = {'L':2,'R':3,'U':0,'D':1}

N = int(input())
move_list = [i for i in input().split()]
xy = [0,0]
for m in move_list:
    next_xy = [xy[0]+dx[move[m]], xy[1]+dy[move[m]]]
    if 0 <= next_xy[0] < N and 0 <= next_xy[1] < N:
        xy = next_xy
print(xy[0]+1,xy[1]+1)