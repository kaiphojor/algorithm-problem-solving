N = int(input())

def isHansu(n):
    digit_list = list(map(int,str(n)))
    if len(digit_list) <= 2:
        return True
    diff = digit_list[0]-digit_list[1]
    for i in range(1,len(digit_list)-1):
        if digit_list[i]-digit_list[i+1] != diff:    
            return False
    return True
hansu_count = 0
for i in range(1,N+1):
    if isHansu(i):
        hansu_count +=1
print(hansu_count)
