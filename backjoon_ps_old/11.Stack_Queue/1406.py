import sys
from collections import deque
input = sys.stdin.readline


left = list(input().strip())
right = deque()
M = int(input().strip())

for _ in range(M):
    a = input()
    if a[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif a[0] == 'D':
        if right:
            left.append(right.popleft())
    elif a[0] == 'B':
        if left:
            left.pop()
    elif a[0] == 'P':
        left.append(a[2])

print("".join(left + list(right)))