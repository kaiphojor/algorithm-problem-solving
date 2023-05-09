"""
def is_subset(c,s,p):
    if c not in s:
        return False
    sorted_s = sorted(s)
    sorted_p = sorted(p)
    while sorted_s:
        c = sorted_s.pop()
        if c not in sorted_p:
            return False
        sorted_p.pop(sorted_p.index(c))
    return True
def is_inclusion(s,p):
    sorted_s = sorted(s)
    sorted_p = sorted(p)
    while sorted_s:
        c = sorted_s.pop()
        if c not in sorted_p:
            return False
        sorted_p.pop(sorted_p.index(c))
    return True
word_list = []
puzzle_list = []
while True:
    input_str = input()
    if input_str == '-':
        break
    word_list.append(input_str)
while True:
    input_str = input()
    if input_str == '#':
        break
    puzzle_list.append(input_str)

for puzzle in puzzle_list:
    puzzle_set = set(puzzle)
    puzzle_dict = dict(zip(puzzle_set,list(0 for _ in range(len(puzzle_set)))))
    for word in word_list:
        for k in puzzle_set:
            if k in word and is_inclusion(word,puzzle):
                puzzle_dict[k] += 1
    minval = min(puzzle_dict.values())
    minres = sorted([k for k,v in puzzle_dict.items() if v==minval])
    maxval = max(puzzle_dict.values())
    maxres = sorted([k for k,v in puzzle_dict.items() if v==maxval])
    print("".join(minres),minval,"".join(maxres),maxval)
    #     # if k in word and 
    # for k in puzzle_set:
    #     # print(k,len(list(filter(lambda w: is_subset(k,w,puzzle),word_list))))
    #     length = len(list(filter(lambda w: is_subset(k,w,puzzle),word_list)))
    #     if length not in freq_dict:
    #         freq_dict[length] = list(k)
    #     else:
    #         freq_dict[length] = freq_dict[length] + [k]
    # minimum = min(freq_dict.keys())
    # maximum = max(freq_dict.keys())
    # print("".join(sorted(freq_dict[minimum])),minimum,"".join(sorted(freq_dict[maximum])),maximum)
        
    
    # puzzle_set = set(puzzle)
    # puzzle_dict = dict(zip(puzzle_set,list(0 for _ in range(len(puzzle_set)))))
    # for k in puzzle_dict.keys():
    #     print(k,len(list(filter(lambda i: is_subset(i, puzzle),word_list))))
    #     # print(k,len(list(filter(lambda i: k in i,word_list))))
    # break
"""
import sys 
input = sys.stdin.readline
dic = []
while True:
    if (a := input().strip()) == '-': break
    dic.append(a)
b = []
while True:
    c = "".join(sorted(input().strip()))
    if c[0] == '#': break
    b.append(c)
    
for d in b:
    s_d = set(d)     
    count_dict = {i:0 for i in s_d}
    max_count = 0
    min_count = 200000
    for letter in s_d:
        for word in dic:
            if letter in word:
                s_word = sorted(word)
                s_board = d
                i = 0
                j = 0
                word_len = len(s_word)
                board_len = len(s_board)
                while i < word_len and j < board_len:
                    if s_word[i] == s_board[j]: i+=1; j+=1
                    else: j+=1
                if i == word_len:
                    count_dict[letter] += 1
    for k in count_dict.keys():
        min_count = min(min_count,count_dict[k])
        max_count = max(max_count,count_dict[k])

    max_list = [] 
    min_list = []
    for k in sorted(s_d):
        if count_dict[k] == min_count:
            min_list.append(k)
        if count_dict[k] == max_count:
            max_list.append(k)
    print("".join(min_list), min_count, "".join(max_list), max_count)