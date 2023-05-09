import sys 
input = sys.stdin.readline

N = int(input())
t = b = l = r = 0
# 정사각형에 다 들어가는 조건 
result = True
xy = []
for i in range(N):
    x, y = map(int,input().split())
    xy.append([x,y])
    if i == 0:
        t = b = x
        l = r = y
    else:
        if t > x : 
            t = x
        if b < x : 
            b = x
        if l > y : 
            l = y
        if r < y : 
            r = y
for x,y in xy:
    if not(x in (t,b) and l <= y <= r or t <= x <= b and y in (l,r)): 
        result = False
        break

if not result:
    print(-1)
elif (b - t) != (r - l) :
    print(-1)
else :
    print( r - l )
# print(b-t, r-l)