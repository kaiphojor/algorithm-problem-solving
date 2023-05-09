self_array = [0 for _ in range(10100)]
i = 1 
self_array[0]=1
while i <= 10000:
    self_array[i + sum(map(int,str(i)))] = 1
    i+= 1
for i,j in enumerate(self_array[:10001]):
    if j == 0:
        print(i)