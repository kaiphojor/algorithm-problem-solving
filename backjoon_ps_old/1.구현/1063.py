K,S,N = input().split()
move_list = list(input() for i in range(int(N)))

move_dict = {'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)}
# 영문 숫자 좌표 -> 데카르트 좌표
def get_coordinate(s):
    return (8-int(s[1]),ord(s[0])-ord('A'))
# 데카르트 좌표 -> 영뭇 숫자 좌표
def get_string_coordinate(c):
    return chr(c[1] + ord('A')) + str(8-c[0])
# 체스 보드 범위를 넘었는지 판별
def is_out_of_board(c):
    return c[0] < 0 or c[0] >= 8 or c[1] < 0 or c[1] >= 8
    
K = get_coordinate(K)
S = get_coordinate(S)

for move in move_list:
    c = move_dict[move]
    new_k = (K[0] +c[0],K[1] + c[1])
    if c[0] + K[0] == S[0] and c[1] + K[1] == S[1]:
        # 이동했을때 겹칠 경우 
        new_s = (S[0] +c[0],S[1] + c[1])
        if is_out_of_board(new_s):
            continue
        K = new_k
        S = new_s
    else:
        # 아닐때
        if is_out_of_board(new_k):
            continue
        else:
            K = new_k
    
print(get_string_coordinate(K))
print(get_string_coordinate(S))