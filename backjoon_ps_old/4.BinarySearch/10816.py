N = int(input())
n_list = list(input().split())
d = dict()
for i in n_list:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
M = int(input())
m_list = list(input().split())
result = []
for i in m_list:
    if i in d:
        result.append(str(d[i]))
    else:
        result.append('0')
print(" ".join(result))