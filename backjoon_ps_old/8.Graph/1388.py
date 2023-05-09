N,M = map(int,input().split())
board = list(input() for _ in range(N))
wood_board_count = 0
# 행에서 연결된 가로판자의 개수 세기
for i in range(N):
    wood_board_count += len(list(filter(lambda x : len(x) > 0,board[i].split('|'))))
# 열끼리 연결된 세로판자의 개수 세기
for j in range(M):
    wood_board_count += len(list(filter(lambda x : len(x) > 0 ,"".join(board[i][j] for i in range(N)).split('-'))))
print(wood_board_count)