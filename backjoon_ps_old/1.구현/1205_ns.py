# 9시 44분
import sys
input = sys.stdin.readline

N, NS, P = map(int, input().split())
rank_list = [0] * P
i = 0
is_ranked = False
if N != 0:    
    for j,e in enumerate(map(int,input().split())):
        rank_list[j] = e    
    # 다른 점수를 가정하고 순회한다. 
    # for j in range(N):

    # 같은 점수를 가정하고 순회한다
    if not is_ranked:
        for j in range(P): 
            # 다른점수 
            if NS > rank_list[j]:
                is_ranked =  True
                i = j
                break
            # 같은 점수 일때
            if NS == rank_list[j]:
                k = j
                while  k < N:
                    if NS == rank_list[k]:
                        k += 1                        
                    else:
                        break
                if k != N:
                    i = j
                    is_ranked = True
                elif NS == 0:
                    i = j
                    is_ranked = True
                break

                # N 까지 닿으면 -1
                # 안닿으면



    

    # for _ in range(N):
    #     cur_score = rank_list[i]
    #     if cur_score == 0:
    #         if i < P:
    #             is_ranked = True
    #             break
    #     if NS > cur_score:
    #         is_ranked = True
    #         while True:
    #             if NS == rank_list[i-1]:
    #                 i -= 1
    #             else:
    #                 break
    #         break
    #     i += 1
else:
    is_ranked = True
print(i+1 if is_ranked else -1)
# 작은 것의 앞에 insert
# 위치 N 이면 배제
# 위치 가장 앞까지 다시 이동
