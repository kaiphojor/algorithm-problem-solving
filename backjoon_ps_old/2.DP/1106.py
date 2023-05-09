"""
https://castlerain.tistory.com/61 의 해법
"""
import sys
input = sys.stdin.readline
inf = 1e9
C, N = map(int, input().split())
pr_list = [tuple(map(int,input().split())) for _ in range(N)]

min_cost = [inf] * (C+100)
min_cost[0] = 0
pr_list.sort(key=lambda x: x[0])

for cost,customer in pr_list:
    for i in range(customer,C+100):
        min_cost[i] = min(min_cost[i-customer]+cost,min_cost[i])
print(min(min_cost[C:]))
