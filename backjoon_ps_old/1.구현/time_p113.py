import time
start = time.time()  # 시작 시간 저장
import sys
input = sys.stdin.readline

N = int(input())

h,m,s = 0,0,0
three_count = 0 
while h != N or m != 59 or s != 59:
    if '3' in str(h):
        three_count += 1
    elif '3' in str(m):
        three_count += 1
    elif '3' in str(s):
        three_count += 1
    s = s + 1 if s < 59  else 0
    if s == 0:
        m += 1
    if m == 60:
        m = 0
        h += 1
print(three_count)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

"""
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
"""