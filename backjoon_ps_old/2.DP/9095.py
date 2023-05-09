"""
4 를 1 2 3 합으로 구현
tree의 
1 1 1  
2 2 11 2
3 4  111 21 3 12
반복문 돌리기 
"""
import sys
sys.setrecursionlimit(10 ** 9)
T = int(input())

def summation(n,s):
    global dp
    if s == 0:
        dp += 1
    elif s == 1:
        summation(n,s-1)
    elif s == 2:
        for i in range(1,2+1):
            summation(n,s-i)
    elif s >= 3:
        for i in range(1, 3 + 1):
            summation(n,s-i)

for _ in range(T):
    dp = 0
    N = int(input())
    summation(N,N)
    print(dp)
    
