import sys
input = sys.stdin.readline

E, S, M = map(int, input().split() )

def esm_translator(e, s, m):
    a = b = c = 1
    year = 1
    while a != e or b != s or c != m:
        a = a + 1 if a < 15 else 1
        b = b + 1 if b < 28 else 1
        c = c + 1 if c < 19 else 1
        year += 1
    print(year)

esm_translator(E, S, M)
