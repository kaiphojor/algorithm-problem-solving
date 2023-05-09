import sys
input = sys.stdin.readline

N, D = map(int, input().split())
path = [ i for i in range(D+1)]
shortest_path = []
for _ in range(N):
    s,e,d = map(int, input().split())
    shortest_path.append([s, e, d])
shortest_path.sort(key= lambda x: x[0])
for start, end, short_path in shortest_path:
    for i in range(end, D+1):
        path[i] = min(path[i],path[start] + short_path + (i-end))
print(path[D])