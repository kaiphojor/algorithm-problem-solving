# 9:07
"""
분기가 너무 많을때 작게 하는것도 좋지만 너무 작게 하려고만 하는것도 미스
"""
B,A = map(int, input().split())
N = int(input())
L = list( list(map(int, input().split())) for _ in range(N))
pd, pl = map(int, input().split())

result = 0
is_ns = True if pd <= 2 else False
for d, l in L:
    if d == pd:
        result += abs(pl-l)
    elif d+pd <= 3 or d+pd >= 7:
        a = A if is_ns else B
        b = (2 * B - l - pl ) if is_ns else (2 * A - l - pl)
        result += min(a + l + pl, a + b)
    else:
        if pd == 1:
            if d == 3:
                result += l + pl
            else:
                result += l + B - pl
        elif pd == 2:
            if d == 3:
                result += A-l + pl
            else:
                result += A-l + B - pl
        elif pd == 3:
            if d == 1:
                result += l + pl
            else:
                result += l + A - pl 
        elif pd == 4:
            if d == 1:
                result += pl + B - l
            else:
                result += A-pl + B-l
print(result)
