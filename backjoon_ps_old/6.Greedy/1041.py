import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
dice = list(map(int, input().split()))
pair = [(i,5-i) for i in range(3)]
if N == 1:
    result = sum(dice) - max(dice)
else:
    m = min(dice)
    m_idx = dice.index(m)
    second_min = 50
    point_sum = m
    for i in range(3):
        if m_idx not in pair[i]:
            val = tuple(dice[x] for x in pair[i])
            cur_min = min(val)
            second_min = min(second_min,cur_min)
            point_sum += cur_min
    line_sum = m + second_min

    # 정육면체 구조. 면 , 모서리, 꼭지점 이용
    result = m * ((N-2) * (N-1) * 4 + (N-2) * (N-2)) + line_sum * ((N-2) * 8 + 4) + point_sum * 4
print(result)