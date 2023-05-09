import sys
input = sys.stdin.readline

pos = input()
a = ord(pos[0])-ord('a')
b = int(pos[1]) - 1
def step_count(x,y):
    count = 0
    next_x,next_y = [-2,-2,2,2,-1,1,-1,1],[-1,1,-1,1,-2,-2,2,2]
    for i in range(8):
        nx, ny = x + next_x[i], y + next_y[i]
        if 0 <= nx < 8 and 0 <= ny < 8:
            count += 1 
    return count

print(step_count(a,b))