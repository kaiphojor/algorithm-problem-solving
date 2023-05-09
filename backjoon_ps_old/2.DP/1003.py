# 피보나치 0,1 출력 개수 세기 
T = int(input())
testCase = [int(input()) for _ in range(T)]
fibo = [[0,0] for _ in range(41)]
fibo[0] = [1,0]
fibo[1] = [0,1]
for i in range(2,41):
    fibo[i] = list(map(sum,zip(fibo[i-1],fibo[i-2])))
for n in testCase:
    print(*fibo[n])