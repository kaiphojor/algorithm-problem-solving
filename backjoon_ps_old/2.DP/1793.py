import sys
input = sys.stdin.readline
def tiling(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        prepre= 1 
        pre = 3
        result = 1
        for i in range(3,n+1):
            result = pre + 2 * prepre 
            prepre = pre
            pre = result
        return result
while True:
    try:
        s = int(input().strip())
        print(tiling(s))
    except:
        break