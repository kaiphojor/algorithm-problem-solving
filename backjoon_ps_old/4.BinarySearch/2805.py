"""
N,M = map(int,input().split())
tree_height_list = list(map(int,input().split()))


bottom = 1
top = max(tree_height_list)
while True:
    mid = (bottom + top) // 2 
    total = 0
    for height in tree_height_list:
        diff = height - mid
        if diff > 0 :
            total += diff
    
    if total > M:
        bottom = mid + 1
    elif total < M:
        top = mid - 1 
    else:
        break
      
print(mid)        
"""
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
tree = sorted(list(map(int,input().split())),reverse=True)
s, mid, e = 0, 0, tree[0] # max
tree_max = tree[-1]
while s <= e:
    mid = (s + e ) // 2
    tree_cut = 0
    for t in tree:
        if t <= mid: 
            break
        tree_cut = tree_cut + t - mid
    if tree_cut < M:
        e = mid - 1 
    else :
        tree_max = mid
        if tree_cut == M:
            break
        s = mid + 1 
    
print(tree_max)