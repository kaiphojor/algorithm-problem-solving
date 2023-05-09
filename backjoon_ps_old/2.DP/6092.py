def hanoi_move(N):
    if N == 1:
        return 1
    return 1 + hanoi_move(N-1) * 2
"""
4 tower hanoi method
4 tower move + 3 tower move + 4 tower move
"""
def optimal_hanoi_move(N,f_hanoi_move):
    min_move = 1
    for i in range(1,N):
        if i == 1:
            min_move = 2 * f_hanoi_move[1] + hanoi_move(N-1)
        else:
            cur_move = 2 * f_hanoi_move[i] + hanoi_move(N-i)
            min_move = cur_move if min_move > cur_move else min_move
    return min_move
        
four_tower_hanoi_move= [0 for _ in range(15)]
for i in range(1,12+1):
    four_tower_hanoi_move[i] = optimal_hanoi_move(i,four_tower_hanoi_move)
    print(four_tower_hanoi_move[i])