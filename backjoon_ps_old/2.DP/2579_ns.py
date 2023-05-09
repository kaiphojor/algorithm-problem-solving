import sys
input = sys.stdin.readline
N = int(input())
s = [0] * 301
for i in range(N):
    s[i] = int(input())
dp = [0] * (300+1)
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[0]+s[2],s[1]+s[2])
for i in range(3,N):
    dp[i] = max(dp[i-2] + s[i],dp[i-3]+s[i-1]+s[i])
print(dp[N-1])