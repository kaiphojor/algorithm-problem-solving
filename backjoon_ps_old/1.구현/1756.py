import sys
input = sys.stdin.readline

D, N = map(int, input().split())
max_len = []
for oven_diameter in map(int,input().split()):
    if not max_len:
        max_len.append(oven_diameter)
    elif max_len[-1] <= oven_diameter:
        max_len.append(max_len[-1])
    else:
        max_len.append(oven_diameter)
pizza_diameter = list(map(int,input().split()))
i = D
j = 0
pizza_depth = []
while i > 0 and j < N:
    i -= 1
    if max_len[i] >= pizza_diameter[j]:
        pizza_depth.append(i)
        j += 1
if j == N:
    print(pizza_depth[-1]+1)
else:
    print(0)