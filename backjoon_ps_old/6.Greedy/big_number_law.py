"""
이것이 코딩테스트다 p.92
큰 수의 법칙

5 8 3
2 4 5 4 6
"""
import sys
input = sys.stdin.readline
N, M, K = map(int,input().strip().split())
first, second, *other = sorted(list(map(int,input().split())),reverse=True)
index_count = K
result = 0
while M > 0:
    if index_count == 0:
        result += second
        index_count = K
    else:
        result += first
        index_count -= 1
    M -= 1
print(result)


"""
첫번째 풀이

import sys
input = sys.stdin.readline
N, M, K = map(int,input().strip().split())
n_list = sorted(list(map(int,input().split())),reverse=True)
index_count = K
result = 0
i = 0
while M > 0:
    if index_count != K and i > 0:
        i -= 1
    if index_count == 0:
        index_count = K
        i = i + 1 if i == 0 else i - 1
    result += n_list[i]
    index_count -= 1
    M -= 1
print(result)
"""