# 삼각형으로 남길 점 3개 조합 추출 
# 사각형 넓이 - 삼각형 주변 공백 넓이
#   max - min * max - min 각 점 간 넓이 1/2 
# 최대값 구하기
import sys, math
from itertools import combinations 
input = sys.stdin.readline

N = int(input())
points = list(list(map(int,input().split())) for _ in range(N))
combination_list = list(combinations(points, 3))
area_list = []
max_area = -1
for comb in combination_list:
    x,y = zip(*comb)
    rectangle_area = abs((max(x)-min(x)) * (max(y)-min(y)))
    blank = 0
    for i in range(3):
        for j in range(i+1,3):
            blank += abs((comb[i][0]-comb[j][0]) * (comb[i][1]-comb[j][1]))
    # blank = (comb[0][0]-comb[1][0]) * (comb[0][1]-comb[1][1]) + (comb[1][0]-comb[2][0]) * (comb[1][1]-comb[2][1]) + (comb[2][0]-comb[0][0]) * (comb[2][1]-comb[0][1])
    blank = abs(blank / 2)
    # area_list.append(rectangle_area-blank)
    max_area = max(rectangle_area-blank,max_area)

max_area = math.trunc(max_area) + 0.5 if (max_area * 10) % 10 == 5 else math.trunc(max_area)
print(max_area)

"""
https://github.com/Leewongi0731/DailyCodeTest/blob/main/%5B%EB%B0%B1%EC%A4%80%20%EC%8B%A4%EB%B2%843%5D%201198%EB%B2%88.py
# 1198번: 삼각형으로 자르기
from itertools import combinations

def getArea( p1, p2, p3 ):
    first = ( p1[0] * p2[1] ) + ( p2[0] * p3[1] ) + ( p3[0] * p1[1] )
    second = ( p1[1] * p2[0] ) + ( p2[1] * p3[0] ) + ( p3[1] * p1[0] )
    re = (first-second) * 0.5
    return abs(re)
################################################################ 
N = int(input())
points = [ list(map(int, input().split())) for i in range(N) ]

result = 0 
for p1, p2, p3 in combinations( points, 3 ):
    area = getArea(p1, p2, p3)
    result = max(result,  area)
print( result )
"""