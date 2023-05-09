"""
N = int(input())
n_dict = dict()
# n_list = [list(map(int,input().split())) for _ in range(N**2) ]
matrix = list(list([0] * N) for _ in range(N))
print(matrix)
for _ in range(N**2):
    row = list(map(int,input().split()))
    student_num,favorite_students = row[0],row[1:]
    n_dict[student_num] = favorite_students
    x,y = 0,0
    max_friendly = 0
    li = list()
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                continue
            # 비어있는 칸 중 좋아하는 학생 인접한 칸 많은 칸
            cur_near_friend = 0
            if i - 1 >= 0 :
                if matrix[i-1][j] in favorite_students:
                    cur_near_friend += 1
            if j - 1 >= 0 : 
                if matrix[i][j-1] in favorite_students:
                    cur_near_friend += 1
            if i + 1 < N :
                if matrix[i+1][j] in favorite_students:
                    cur_near_friend += 1
            if j + 1 < N : 
                if matrix[i][j+1] in favorite_students:
                    cur_near_friend += 1
            if max_friendly < cur_near_friend:
                max_friendly = cur_near_friend
                x,y = i,j
                continue
print(n_dict)
"""
# https://foameraserblue.tistory.com/176 
# 중간에 꼬여서 결국은 봄

import sys 

input = sys.stdin.readline
n = int(input())
students_list = [] 
table_list = [[0 for j in range(n)] for i in range(n)]
dic = {}
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n**2):
    students_list.append(list(map(int,input().split())))

def cnt(f_list,i,j):
    count = 0
    f_count = 0 
    # 4 방향 check
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if nx >=0 and nx < n and ny >=0 and ny < n:
            # 빈칸 count
            if table_list[ny][nx] == 0:
                count += 1
            if f_list:
                if table_list[ny][nx] in f_list:
                    f_count += 1
    return count, f_count

for s in students_list :
    friend = [] 
    # table_list 안에 내가 좋아하는 친구가 있는지 확인
    for i in range(1,5): 
        if s[i] in dic:
            friend.append(s[i])
    
    # 좋아하는 친구가 이미 자리를 잡았을 때 
    if friend:
        # 모든 자리 탐색
        # 주변에 친한친구 수, 근처 비어있는 곳의 갯수, i, j 좌표
        max_cnt = [] 
        for i in range(n):
            for j in range(n):
                if table_list[i][j] == 0:
                    result, f_cnt = cnt(friend, i, j)
                    if not max_cnt:
                        max_cnt = [f_cnt,result,i,j]
                    if f_cnt > max_cnt[0]:
                        max_cnt = [f_cnt, result, i,j]
                    if f_cnt == max_cnt[0] and result > max_cnt[1]:
                        max_cnt = [f_cnt, result, i,j]
        # 자리 찾고 앉히는 과정
        table_list[max_cnt[2]][max_cnt[3]] = s[0] 
        dic[s[0]] = s[1:]
    
    # 아직 자리를 잡기 전
    else:
        # 비어있는 곳 갯수, i,j 좌표 
        max_cnt = [] 
        for i in range(n):
            for j in range(n):
                if table_list[i][j] == 0:
                    result, f_cnt = cnt(friend, i,j) 
                    if not max_cnt:
                        max_cnt = [result, i,j]
                    elif result > max_cnt[0]:
                        max_cnt = [result,i,j]
        # 자리 찾은다음 앉히기
        table_list[max_cnt[1]][max_cnt[2]] = s[0]
        dic[s[0]] = s[1:]
# 다 앉힌 다음 점수 계산 
# 0:0 / 1:1 / 2:10 / 3 :100 / 4:1000
point =0
for i in range(n):
    for j in range(n):
        f_list = dic[table_list[i][j]]
        empty_val, f_cnt = cnt(f_list,i,j)
        if f_cnt == 0:
            point += 0
        elif f_cnt == 1:
            point += 1
        elif f_cnt == 2:
            point += 10
        elif f_cnt == 3:
            point += 100
        else :
            point += 1000

print(point)