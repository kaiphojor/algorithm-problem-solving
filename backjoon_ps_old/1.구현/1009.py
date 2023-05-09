import sys
input = sys.stdin.readline
T = int(input())
result = []
for _ in range(T):
    a,b = map(int,input().split())
    c = pow(a,b,10)
    c = c if c > 0 else 10
    result.append(c)
for r in result: 
    print(r) 