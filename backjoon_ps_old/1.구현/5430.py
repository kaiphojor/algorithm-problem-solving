import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    function_list = input().strip()
    n = int(input())
    comma_input = input().strip('\n []').split(',')
    n_list = [] if '' in comma_input else list(comma_input)
    is_error = False
    is_reverse = False
    start, end = 0, n
    for f in function_list:
        if "R" == f:
            is_reverse = not is_reverse
        elif end - start <= 0:
            is_error = True
            break
        elif is_reverse:
            end -= 1
        else:
            start += 1
    if is_error:
        result.append("error")
    else:
        n_list = list(reversed(n_list[start:end])) if is_reverse else n_list[start:end]
        result.append('['+','.join(n_list)+']')
for r in result:
    print(r)
