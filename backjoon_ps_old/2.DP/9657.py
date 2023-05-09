l = [True]* 1000
for i in range(1000):
    if i in (1-1,3-1,4-1):
        l[i] = True
    elif i == 2:
        l[i] = False
    elif False in (l[i-1],l[i-3],l[i-4]):
        l[i] = True
    else:
        l[i] = False
print("SK") if l[int(input())-1] else print("CY")

"""
시간초과
def leftover(n):
    if n in (1,3,4):
        return True
    elif n == 2:
        return False
    else:
        for i in (1,3,4):
            if leftover(n-i) == False:
                return True
        return False

print("SK") if leftover(int(input())) else print("CY")
"""