"""

"""

from itertools import permutations
N = int(input())

permutation_list = list(permutations(range(1,N+1)))
for i in permutation_list:
    print(*i)