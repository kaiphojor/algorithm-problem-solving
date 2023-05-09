import sys
input = sys.stdin.readline
N = int(input())
i = 0
student_code = [input().strip() for _ in range(N)]
while True:
    i += 1
    code_set = set(map(lambda x: x[-i:],student_code))
    if len(code_set) == N:
        break
print(i)