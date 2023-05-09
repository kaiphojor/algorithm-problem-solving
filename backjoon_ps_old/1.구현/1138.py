N = int(input())
left_taller_list = list(map(int,input().split()))
n_list = [i for i in range(1,N+1)]
for i,left_count in reversed(list(enumerate(left_taller_list))):
    element = n_list.pop(n_list.index(i+1))
    j = 0
    while left_count > 0:
        if n_list[j] > element:
            left_count -= 1
        j += 1
    while j + 1 < N:
        if n_list[j] > element :
            break
        j +=1
    n_list.insert(j,element)
print(" ".join(map(str,n_list)))