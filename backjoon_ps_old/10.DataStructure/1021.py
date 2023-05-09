import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
position_list = list(map(int,input().split()))
queue = deque(list(i for i in range(1,N+1)))
count = 0
for pos in position_list:
    if pos != queue[0]:
        idx = queue.index(pos)
        left_dist = idx
        right_dist = len(queue) - idx
        if left_dist < right_dist :
            while left_dist > 0 : 
                queue.append(queue.popleft())            
                left_dist -= 1
                count += 1
        else :
            while right_dist > 0 : 
                queue.appendleft(queue.pop())           
                right_dist -= 1
                count += 1
    queue.popleft()

print(count)

