"""
번호 
백트래킹
N,
비용행렬 
시작 정해져 있음. visited 똑같음
완전탐색 - 시간초과
한줄마다 탐색 - 틀림
전체 순회 조건 - 회귀 조건 추가 - 틀림
permutation 적용 - 틀림

"""
"""
import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
W = list( list(map(int,input().split())) for _ in range(N) )
permutations = list(permutations(range(N),N))

def filterSelf(x):
    for i,e in enumerate(x):
        if i == e:
            return False
    visited = set()
    cur = 0
    for _ in range(N):
        visited.add(cur)
        cur = x[cur]
    return len(visited) == N and cur == 0

print(min(list(map(lambda x : sum(W[i][x[i]] for i in range(N)), filter(filterSelf, map(list,permutations))))))
"""
"""
jvisited = []
sum_list = []



def checkConnected(loc):
    cur = 0
    visited = set()
    for _ in range(N):
        visited.add(cur)
        cur = loc[cur]
    return len(visited) == N

def bt(start,cost):

    if start == N:        
        if checkConnected(jvisited):
            sum_list.append(cost)
    
    for j in range(N):
        if start != j and j not in jvisited:
            jvisited.append(j)
            bt(start + 1,cost + W[start][j])
            jvisited.pop()
bt(0,0)
print(min(sum_list))
"""

from itertools import  permutations
import sys,math

def solution():
    n = int(sys.stdin.readline())
    city = []
    res = math.inf

    for _ in range(n):
        city.append(list(map(int,sys.stdin.readline().rstrip().split())))

    routes = list(permutations(range(n)))

    for route in routes:
        if city[route[-1]][route[0]] == 0:
            continue

        temp = 0
        flag = False

        for i in range(n-1):
            if city[route[i]][route[i+1]] == 0:
                flag = True
                break

            temp += city[route[i]][route[i+1]]
        
            if temp >= res:
                flag = True
                break

        if flag:
            continue

        temp += city[route[-1]][route[0]]
        res = min(res, temp)
        
    print(res)

solution()