import sys
input = sys.stdin.readline
K, N = map(int,input().split())
lan_cable = [int(input()) for _ in range(K)]# sorted([int(input()) for _ in range(K)])

s, e = 1, sum(lan_cable) // N + 1
old_mid = mid = 0
# = 포함하면 e mid -1 해도 되고 아니면 안된다
while s < e:
    mid = (s + e) // 2
    cut_count = sum(x//mid for x in lan_cable)#sum(map(lambda x: x//mid,lan_cable))
    if N <= cut_count:
        old_mid = mid
        s = mid + 1
    else:
        e = mid 

print(old_mid)

"""
예시
4 11
802
743
457
539


반례:

9 3785
73085
6747
87849
30807
79944
26905
92558
15313
2016
답: 109

출력: 110
"""