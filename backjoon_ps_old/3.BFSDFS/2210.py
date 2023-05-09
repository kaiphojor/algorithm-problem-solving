import sys
input = sys.stdin.readline

board = [list(input().split()) for _ in range(5)]
six_digit_num = []
dx,dy = [-1,1,0,0],[0,0,-1,1]

# dfs로 문자열 구성
def dfs(x1,y1,s):
    if len(s) >= 6:
        if s not in six_digit_num:
            six_digit_num.append(s)
        return
    s = s + board[x1][y1]
    for i in range(4):
        nx,ny = x1+dx[i],y1+dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 :
            dfs(nx,ny,s)

# 숫자판 순회하며 dfs 수행
for i in range(5):
    for j in range(5):
        dfs(i,j,"")
print(len(six_digit_num))
