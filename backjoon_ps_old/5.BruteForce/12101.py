"""
순열 만들기  - x
규칙성 찾기

해당 순열 찾기 - x
사전 순 정렬 - x
문자열 조합하기

알고리즘 모를땐 찾아보기
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
result_count = 0
result = "-1"
def back_tracking(ar):
    global result_count

    if result_count > k:
        return

    if (s :=sum(ar)) == n:
        result_count += 1

        if result_count == k:
            global result
            result = "+".join(str(i) for i in ar)
        return

    residue = n - s
    for i in range(1,3+1):
        if residue >= 1:
            arr.append(i)
            back_tracking(ar)
            arr.pop()

back_tracking(arr)
print(result)