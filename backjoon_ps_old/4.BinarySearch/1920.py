n = int(input())
a = sorted(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
# a 이분 탐색
for i in b:
    isFind = False
    start = 0 
    end = len(a) - 1
    while start <= end :
        mid = (start + end) // 2 
        if a[mid] == i:
            isFind = True
            break
        elif a[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    print(1 if isFind else 0)