"""
가장 긴 증가하는 부분 수열
증가 = 같지 않음
구하는 법
작은 것 중 + 1 했을 때 가장 큰 것

6
5 2 4 8 7 2

test case 에서 max 아닌 값이 나오는 것을 발견
부분집합이 꼭 첫번째에서만 나오지 않음. 
"""
import sys
input = sys.stdin.readline

N = int(input())
dp = [1] * N
seq = list(map(int,input().split()))
for i in range(1,N):
    j = i-1
    while j >= 0:
        if seq[j] < seq[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        j -= 1

print(max(dp))
