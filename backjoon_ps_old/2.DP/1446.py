# https://jinho-study.tistory.com/1014의 풀이
import sys
input = sys.stdin.readline
N, D = map(int,input().split())
n_list = list(list(map(int,input().split())) for _ in range(N))
# n_list = list(filter(lambda x : x[1] - x[0] > x[2] and x[1] <= D,n_list))
# n_list.sort(key=lambda x: x[1]-x[0]-x[2],reverse=True)
# result_list = []
# print(n_list)
# for n in n_list:
#     print(n)
#     print(n[1]-n[0]-n[2])
# for i in n_list:
#     saved_length = i[1]-i[0]-i[2]
#     is_between_range = False
#     for j in result_list:
#         if j[0] <= i[0] < j[1] or j[0] < i[1] <= j[1]:
#             is_between_range = True
#             break
#     if not is_between_range :
#         result_list.append(i)
#         D -= saved_length
#         print(D, saved_length)
# print(D)
    #범위에 대한 필터링
dist = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        # 이전거리 + 1 이 짧으면 교체
        dist[i] = min(dist[i],dist[i-1]+1)
    for s,e,d in n_list:
        # 거리가 현재위치에서 시작하고, 지름길을 통해 조금이라도 더 짧아질 수 있다면 교체한다
        if i == s and e <= D and dist[i]+d < dist[e] : 
            dist[e] = dist[i] + d
print(dist[D])
            