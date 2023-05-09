from functools import reduce
N = int(input())
P = sorted(map(int,input().split())) 
S = reduce(lambda x,y : x+y,[sum(P[:i+1]) for i,_ in enumerate(P)])
print(S)


