import sys
input = sys.stdin.readline

switch_num = int(input())
s = list(map(int, input().split()))
student_num = int(input())
student_list = [ list(map(int, input().split())) for _ in range(student_num)]

bin_swap = [1, 0]
for student in student_list:
    if student[0] == 1:
        for i in range(1,switch_num+1):
            if i % student[1] == 0:
                # s[i-1] ^= 1 # xor swap
                s[i-1] = bin_swap[s[i-1]]
    else:
        a, b = student[1],1
        s[a-1] = bin_swap[s[a-1]]
        while 0 <= (c := a - b - 1) and ( d:= a + b - 1) < switch_num:
            if s[c] == s[d]:
                s[c] = s[d] = bin_swap[s[d]]
                b += 1
            else: break

for i,e in enumerate(s):
    print(e,end=" ")
    if (i+1) % 20 == 0:
        print()