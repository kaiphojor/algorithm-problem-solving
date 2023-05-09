import sys
input = sys.stdin.readline
M, N = map(int, input().split())
n_list = [i for i in map(int, input().split())]
s,e = 1,max(n_list)
max_snack_len = 0
while s <= e:
    mid = (s + e) // 2
    snack_count = sum(map(lambda y: y // mid,filter(lambda x: x>=mid , n_list)))
    if snack_count >= M:
        max_snack_len = max(max_snack_len,mid)
        s = mid + 1
    else:
        e = mid - 1
print(max_snack_len)