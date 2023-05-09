# 1120번 문제
# Brute force가 key
def get_diff(a,b):
    return len([i for i,j in zip(a,b) if i != j])

a, b = map(str,input().split())
min_diff = len_a = len(a)
len_b = len(b)
if len_a == len_b: 
    min_diff = get_diff(a,b)
else : 
    for i in range(len_b - len_a + 1):
        cur_diff = get_diff(a,b[i:i+len_a])
        min_diff = cur_diff  if cur_diff < min_diff else min_diff
print(min_diff)