import sys
input = sys.stdin.readline

Lx, Ly, N = map(int,input().split())
box_list = [] 
for _ in range(N):
    lx, ly, lz, px, py = map(int,input().split())