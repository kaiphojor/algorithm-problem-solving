from itertools import combinations
L = int(input())
S = sorted(list(map(int,input().split())))
n = int(input())
start = 1
end = 1

for i,e in enumerate(S):
    if e < n:
        start = e + 1
        if i < L-1:
            end = S[i+1] - 1
        else:
            end = S[i]-1        
    elif e > n and i == 0:
        end = e - 1
    
range_count = 0

for i in range(start,end):
    for j in range(i+1,end+1):
        if n in range(i,j+1):
            range_count +=1 
print(range_count)

