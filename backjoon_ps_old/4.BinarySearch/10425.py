import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def fibonacci(m):
    if m <= 2: return 1
    else: return fibonacci(m-1) + fibonacci(m-2)
def inverse_fibonacci(n):
    if n == 1: return 2
    a,b,i = 1,1,3
    while (c := a + b) != n:
        a = b
        b = c
        i += 1
    return i
T = int(input())
for _ in range(T):
    F = int(input())
    print(inverse_fibonacci(F))