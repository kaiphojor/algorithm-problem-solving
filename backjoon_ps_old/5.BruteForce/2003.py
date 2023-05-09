import sys
input = sys.stdin.readline
N, M = map(int, input().split())
n_seq = list(map(int, input().split()))
seq_count = 0
start = end = 0
seq_sum = 0
while start < N:
    while seq_sum < M and end < N:
        seq_sum += n_seq[end]
        end += 1
    if seq_sum == M:
        seq_count += 1
        seq_sum -= n_seq[start]
        start += 1
    elif seq_sum > M:
        seq_sum -= n_seq[start]
        start += 1
    else:
        start += 1
print(seq_count)