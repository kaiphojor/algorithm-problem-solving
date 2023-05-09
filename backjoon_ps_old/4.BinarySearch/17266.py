N = int(input())
M = int(input())
m_list = list(map(int,input().split()))

min_len = 1
for i,m in enumerate(m_list):
    if i == 0:
        min_len = m if min_len < m else 1
    else:
        while m_list[i-1] + min_len < m - min_len:
            min_len += 1
    if i == M-1:
        while m + min_len < N:
            min_len += 1
print(min_len)

