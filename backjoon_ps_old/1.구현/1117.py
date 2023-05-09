import sys 
input = sys.stdin.readline
W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

# 가로로 겹치는 기준선, 세로 접히는 횟수
v_fold_count = c+1
overlap_width = min(f, abs(W - f))
dyed_area = (x2-x1) * (y2-y1)
total_dyed_area = 0

# 기준선이 색칠영역 왼쪽 / 안쪽 / 오른쪽 에 있을 경우
if overlap_width <= x1:
    total_dyed_area = v_fold_count * dyed_area
elif overlap_width < x2 :
    total_dyed_area = v_fold_count * dyed_area + v_fold_count * (overlap_width - x1) * (y2-y1)
else :
    total_dyed_area = v_fold_count * 2 * dyed_area

print(W * H - total_dyed_area)