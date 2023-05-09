import sys
input = sys.stdin.readline

N = int(input())
average_score = [float(input()) for _ in range(N)]
result = 1
while True:
    i = 0
    while i < N:
        sum_score = average_score[i] * result
        print("i", i, "result : ",sum_score)
        if sum_score.is_integer() or sum_score * 1000 % 1000 >= 900:
            i += 1
        else :
            break
    if i == N:
        break
    result += 1
print(result)

# sum_score * 1000 % 1000
# sum_score - int(sum_score) * 1000