from itertools import permutations
N = int(input())
seq = list(map(int, input().split()))
def diff_sum(s):
    result = 0
    for i in range(1,N):
        result += abs(s[i]-s[i-1])
    return result
print(max(map(diff_sum,permutations(seq,N))))
