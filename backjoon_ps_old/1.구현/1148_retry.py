import sys
input = sys.stdin.readline
w_list = []
c_list = []
def count_up(x):
    c_count[x] += 1
while((word := input().strip()) != '-'):
    w_list.append(sorted(word))
c_list = sorted(list(set(c_list)))
while((board := input().strip()) != '#'):
    board = sorted(board)
    c_list = sorted(list(set(board)))
    c_count = {char:0 for char in c_list}

    for word in w_list:
        w_idx = b_idx = 0 
        w_len,b_len = len(word),len(board)
        while b_idx < b_len and w_idx < w_len:
            if word[w_idx] == board[b_idx]:
                w_idx += 1
            b_idx += 1
        if w_idx == len(word):
            for w_char in set(word):
                c_count[w_char] += 1
    min_val = min(c_count.values())
    max_val = max(c_count.values())
    min_char = "".join(filter(lambda x: c_count[x] == min_val,c_list))
    max_char = "".join(filter(lambda x: c_count[x] == max_val,c_list))
    print(min_char,min_val,max_char,max_val)