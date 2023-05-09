def factorial(n):
    if n == 0 :
        return 1
    return n * factorial(n-1)
T = int(input())
test_result = list()

for i in range(T):
    N,M = map(int,input().split())
    combination_result = factorial(M) // (factorial(M-N) * factorial(N))
    test_result.append(combination_result)
for j in test_result:
    print(j)

