import sys
input = sys.stdin.readline

N = int(input())
members = []
for i in range(N):
    inp =  input().split()
    inp[0] = int(inp[0])
    members.append([i] + inp)

members.sort(key= lambda x : (x[1],x[0]))

for m in members:
    print(m[1], m[2])