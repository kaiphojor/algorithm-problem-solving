import copy
N = int(input())
is_friend = [list(input()) for _ in range(N)]
friend_list = {i:set(j for j,x in enumerate(is_friend[i]) if x == 'Y') for i in range(N)}

two_friend_list = copy.deepcopy(friend_list)
for i in range(N):
    for j in list(friend_list[i]):
        two_friend_list[i].update(friend_list[j])
maximum = 0
for i in range(N):
    if i in two_friend_list[i]:
        two_friend_list[i].remove(i)
    maximum = max(len(two_friend_list[i]),maximum)
print(maximum)