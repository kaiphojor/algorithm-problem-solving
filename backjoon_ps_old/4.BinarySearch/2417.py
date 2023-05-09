import sys
input = sys.stdin.readline

N = int(input())
def get_min_root(n):
    s,e = 1,n
    result = 2 ** 63 - 1
    if n == 0:
        return 0
    while s <= e:
        mid = (s + e) // 2
        if (squared := mid ** 2) < n:
            s = mid + 1
        else:
            result = min(result, mid)
            e = mid - 1
    return result

print(get_min_root(N))