# 출처 
# https://velog.io/@gglifer/%EB%B0%B1%EC%A4%80-1660-%EC%BA%A1%ED%8B%B4-%EC%9D%B4%EB%8B%A4%EC%86%9C
import sys
input = sys.stdin.readline

N = int(input())

dp = [i for i in range(N+1)]
i = j = k = 1 
while k <= N:
    for n in range(1,N+1):
        if n >= k:
            dp[n] = min(dp[n], dp[n-k]+1)
    i += 1;j += i; k += j
print(dp[N])