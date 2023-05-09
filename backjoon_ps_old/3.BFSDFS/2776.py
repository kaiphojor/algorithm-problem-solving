def bin_tree_search(arr,num):
    l = len(arr)
    start = 0 ; end = l-1
    while start <= end :
        mid = (start + end) // 2
        if arr[mid] == num:
            return True
        elif arr[mid] < num :
            start = mid + 1
        else:
            end = mid - 1
    return False
# import sys
# input = sys.stdin.readline
T = int(input()) 
for _ in range(T):
    N = int(input())
    n_list = sorted(list(map(int,input().split())))
    M = int(input())
    m_list = list(map(int,input().split()))
    for i in m_list :
        if bin_tree_search(n_list,i):
            print(1)
        else:
            print(0)