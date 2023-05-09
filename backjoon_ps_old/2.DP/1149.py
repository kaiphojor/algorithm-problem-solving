N = int(input())
rgb_list = list(list(map(int,input().split())) for _ in range(N))
min_list = [[0,0,0] for _ in range(N)]
min_list[0] = rgb_list[0]
for i in range(1,N):
    min_list[i][0] = rgb_list[i][0] + min(min_list[i-1][1],min_list[i-1][2])
    min_list[i][1] = rgb_list[i][1] + min(min_list[i-1][0],min_list[i-1][2])
    min_list[i][2] = rgb_list[i][2] + min(min_list[i-1][0],min_list[i-1][1])
print(min(min_list[N-1]))