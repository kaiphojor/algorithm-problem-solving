import sys
input = sys.stdin.readline

N = int(input().strip())
A,B = map(int,input().split())
p_list = set(tuple(map(int,input().split())) for _ in range(N))
count = 0
for a,b in p_list:
    if (a+A,b) in p_list and (a,b+B) in p_list and (a+A,b+B) in p_list:
        count += 1
print(count)