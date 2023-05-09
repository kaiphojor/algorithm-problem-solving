# 백준 1206 python 
"""
문항 -> 0 <= 범위 <= 10
문항 평균 소수점 세자리 자르기
평균점수 안다. 사람수 모른다
평균 점수 input -> 사람수 output
"""
from functools import reduce
import sys
input = sys.stdin.readline
def gcd(a, b):
    if a < b:
        a, b = b, a
    while True:
        c = a % b
        if c == 0:
            return b
        a,b = b,c
def lcm(a, b):
    return a * b // gcd(a,b)

min_people_count = []
for i in range(int(input())):
    f = float(input())
    # 문항 점수 총점은 정수
    val = 1
    while not (val * f).is_integer():
        val += 1
    min_people_count.append(val)
print(reduce(lcm,min_people_count))
