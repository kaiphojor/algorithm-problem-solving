"""
a -> b 
* 2 *10 + 1
어느쪽이든 증가 -> 목표수보다 커지면 x
필요한 것 - depth, value, return min_depth
min depth = global value
"""
A, B = map(int, input().split())
oc = 10 ** 9

def dfs(d, cur):
    global oc

    if cur > B:
        return
    if cur == B:
        oc = min(oc, d)
        return

    dfs(d+1,cur * 2)
    dfs(d+1,cur * 10 + 1)

dfs(0,A)
print(oc+1 if oc != 10 ** 9 else -1)