"""
import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
n_list = list(map(int, input().split()))

s_count = 0
for i in range(1,N+1):
    comb_iter = combinations(n_list, i)
    for j in comb_iter:
        if sum(j) == S:
            s_count += 1

print(s_count)
"""
# 나중에 두고 봐야


import sys
input = sys.stdin.readline

N, S = map(int,input().split())
n = list(map(int,input().split()))
s_count = 0 
def backtracking(i,p):
    global s_count
    if i >= N : 
        return
    p.append(n[i])
    if sum(p) == S:
        s_count += 1
        return
    backtracking(i+1,p)
    p.pop()

for i in range(N):
    backtracking(i, [])
    # for j in range(i,N):
    #     if sum(n[i:j+1]) == S:
    #         s_count += 1

print(s_count)