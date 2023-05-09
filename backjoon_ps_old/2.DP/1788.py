import sys
n = int(input())

def negative_fibonacci(N):
    if N < 0 and N % 2 == 0:
        print(-1)
    elif N == 0:
        print(0)
    else:
        print(1)
    N = abs(N)
    if N <= 1: print( N )
    else:
        a,b,c = 0,1,0
        for i in range(2,N+1):
            c = a + b
            a = b
            b = c
        return print(c % 1000000000)

negative_fibonacci(n)