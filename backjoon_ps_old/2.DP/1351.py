import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
N, P, Q = map(int, input().split())
dic = defaultdict(int)
dic[0] = 1
def inf_seq(n):
    if dic[n] == 0:        
        dic[n] = inf_seq(n//P)+inf_seq(n//Q)
    return dic[n]
print(inf_seq(N))