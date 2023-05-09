import sys
input = sys.stdin.readline
N, M = map(int, input().split())
max_value = 0
for _ in range(N):
    max_value = max(max_value,min(map(int,input().split())))
print(max_value)

"""
3 3
3 1 2
4 1 4
2 2 2
2 4
7 3 1 8
3 3 3 4
"""