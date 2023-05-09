"""
로직을 주석으로 쓰고 구현
입력을 받는다
t = 0
t 증가
받으면서 dict key[t] 가 있으면 제거한다
dic value 합 + 신규값이 기준치 이하라면 t + w 추가
아니라면 그냥
dict에 키가 있는지 확인 후 탈출 
"""
from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
a = deque( map(int, input().split()))
b_dict = dict()
t = 0

while True:
    # 시간 증가
    t += 1

    # 다리 끝에 도착한 트럭이 있는지 확인
    if t in b_dict:
        del b_dict[t]
    
    if a:
        # 갈 트럭이 있고, 다리 하중이 트럭 진입을 허용할 때 
        if sum(b_dict.values()) + a[0] <= L:
            b_dict[t+w] = a[0]
            a.popleft()

    # 진입할 트럭도 없고, 다리에 트럭도 없을 때
    elif not b_dict:        
        break

print(t)
    
    

    
