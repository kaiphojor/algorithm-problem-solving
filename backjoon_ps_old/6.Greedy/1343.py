P = input()
i = 0
flag = True
while True:
    c = P.find('.',i)
    if c == -1:
        if P[-1] == 'X':
            c = len(P)
        else:
            break
    cur = P[i:c]
    l = len(cur)
    if l % 2 == 1:
        flag = False
        break
    div,mod = divmod(l,4)
    s = div * "AAAA" + mod//2 * "BB"
    P = P[:i] + s + P[c:]
    i = P.find("X",c)
    if i == -1:
        break
print(P if flag else -1)

"""
잘 푼사람 풀이
board = input()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)

출처: https://s0ng.tistory.com/entry/백준-그리디-알고리즘-폴리오미노-1343번-파이썬-python
"""