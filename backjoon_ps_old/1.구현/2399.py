n = int(input())
x = list(map(int,input().split()))
x.sort()
"""
규칙성 찾기
차의 절대값의 총합
0 a b c
a 0 d e
b d 0 f
c e f 0
이므로 대각선 반의 합만 구하면 됨

1 2 3 4의 경우(정렬 후)
4 4 4      3 2 1
  3 3   -    2 1
    2          1
이므로 두 합의 차를 계산함
"""
print(2 * (sum(x[i] * i for i in range(n-1,0,-1)) - sum(x[n-1-i] * i for i in range(n-1,0,-1))))
