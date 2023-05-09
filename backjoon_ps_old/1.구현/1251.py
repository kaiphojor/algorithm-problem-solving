import sys
from itertools import combinations
input = sys.stdin.readline
s = input().strip()
comb = combinations(range(1,len(s)),2)
result = 'z' * 50
for t in comb:
    x, y = t
    li = ''.join(reversed(s[:x]))+''.join(reversed(s[x:y]))+ ''.join(reversed(s[y:]))
    result = result if result < li else li
print(result)