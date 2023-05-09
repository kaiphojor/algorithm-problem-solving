# 경우의 수 , 분기를 잘 파악해야 한다
T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    distance =  (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
    reach = r1 + r2
    if distance == 0:
        if r1 == r2: 
            print(-1)
        else:
            print(0)
    elif distance == reach:
        print(1)
    elif distance < reach:
        min_val,max_val = min(r1,r2), max(r1,r2)
        if min_val + distance == max_val :
            print(1)
        elif min_val + distance < max_val :
            print(0)
        else:
            print(2)
    else:
        print(0)