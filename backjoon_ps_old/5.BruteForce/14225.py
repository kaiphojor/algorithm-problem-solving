# 14225
from itertools import combinations
N = int(input())
s = list(map(int,input().split()))
is_calculate = [False] * (sum(s)+2)
is_calculate[0] = True
for i in range(1,N+1):
    for j in map(sum,combinations(s,i)):
        is_calculate[j] = True
for n in range(1,sum(s)+2):
    if is_calculate[n] == False:
        print(n)
        break
