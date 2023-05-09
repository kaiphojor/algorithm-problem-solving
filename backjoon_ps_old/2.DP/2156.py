"""
포도주 제일 많이 마시기
MAX - 포도주량
선택 - 포도주잔 순서
제약 3 연속 금지
두개 연속일 때는 x 
처음 들어갈 때 step 기록
step = step + 1
step = 1
1 6 1
2 6 + 10 = 16 2 
3 6 + 13 < 10 + 13 = 23 2
4 16 + 9 : 23  25 1 
5 23 + 8 : 25 + 8 = 33 2
6 25 + 1 : 33 + 0 = 33 

결국 dp 시간초과 에 약한듯
"""
import sys
sys.setrecursionlimit(10**6)
n = int(input())
dp = [0] * (n+1)
w = [0] * (n+1)
for i in range(n):
    w[i+1] = int(input())

def find_maximum_consumption(i):
    a = dp[i-3] + w[i-1] + w[i]
    b = dp[i-2] + w[i]
    c = dp[i-1]
    dp[i] = max(a,b,c)

dp[1] = w[1]
if n > 1:
    dp[2] = w[1] + w[2]
if n > 2:
    dp[3] = max(w[1] + w[3],w[2]+w[3],dp[2])
if n > 3:
    for seq in range(4,n+1):
        find_maximum_consumption(seq)

print(dp[n])



