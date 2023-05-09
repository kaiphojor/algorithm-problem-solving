import sys 
input = sys.stdin.readline

N = int(input().strip())

loss_list = [i for i in map(int,input().split())]
bliss_list = [i for i in map(int,input().split())]
loss_bliss = list(zip(loss_list,bliss_list))

def dp_sum(N,i,loss,bliss):
    if loss <= -100:
        return 0
    if i == N:
        return bliss
    return max(dp_sum(N,i+1,loss,bliss),dp_sum(N,i+1,loss-loss_bliss[i][0],bliss+loss_bliss[i][1]))
current_bliss = dp_sum(N,0,0,0)

print(current_bliss)
