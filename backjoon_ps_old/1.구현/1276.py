# 계획적으로 짜고 꼼꼼히 살펴봐야 시간을 줄인다
import sys 
input = sys.stdin.readline

N = int(input())
platform_list = sorted([ list(map(int,input().split())) for _ in range(N) ],key=lambda x: x[0])
# 겹치는 부분에 대한 전처리가 문제였다 
for i in platform_list:
    i[2] -= 1
result = 0

for i in range(N):

    altitude = a = b = platform_list[i][0]

    l,r = platform_list[i][1],platform_list[i][2]

    for j in range(0,i):
        if platform_list[j][1] <= l and l <= platform_list[j][2] :
            a = altitude - platform_list[j][0]
        if  platform_list[j][1] <= r and r <= platform_list[j][2] :
            b = altitude - platform_list[j][0]
    result = result + a + b
print(result)
