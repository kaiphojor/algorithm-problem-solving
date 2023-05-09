name_str = input().strip()
no_answer_message = "I'm Sorry Hansoo"
name_length = len(name_str)
flag = True
name_list = sorted(name_str,reverse=True)
p_list = []
i = 0
middle = ""

if name_length % 2 == 1:
    is_solo_odd = False
    for c in set(name_list):
        if name_list.count(c) % 2 == 1:
            if not is_solo_odd:
                is_solo_odd = True
            else:
                is_solo_odd = False
                flag = False
                break
    
while i < name_length and flag:
    if i + 1 < name_length:
        if name_list[i] == name_list[i+1]:
            p_list = [name_list[i]] + p_list + [name_list[i+1]]
            i += 2
        elif name_length % 2 == 1:
            middle = name_list[i]
            i += 1
        else:
            flag = False
            break
    elif name_length % 2 == 1:
        middle = name_list[i]
        i += 1
    else:
        flag = False
        break
if middle != "":
    p_list.insert(name_length//2,middle)
        
if flag:
    print("".join(p_list))
else:
    print(no_answer_message)




"""
for i,e in enumerate(reverse_name_list):
if name_length % 2 == 1:
    for c in char_list:
        if name_list.count(c) % 2 == 1:
            middle = name_list.pop(name_list.index(c))
    if middle == "":
        flag = False
else:
    for c in char_list:
        if name_list.count(c) % 2 == 1:
            flag = False
            break
if flag:
    half_list = [c for i,c in enumerate(name_list) if i % 2 == 0]
    palindrome_list = half_list + [middle] + list(reversed(half_list))
    print("".join(palindrome_list))
else:
    print(no_answer_message)














    print(name_list)
else:
    print(no_answer_message)

if name_length % 2 == 0:
    for
else:


flag = True
for i,e in enumerate(char_list):
    if i == len(char_list) - 1:
        # 짝수일 때
        if name_length % 2 == 0 and name_str.count(char_list[i]) != 2:
            flag = False
            break
        if name_length % 2 == 1 and name_str.count(char_list[i]) != 1:
            flag = False
            break
    if name_str.count(char_list[i]) != 2:
        flag = False
        break
if flag:
    half_index = name_length // 2
    palindrome_list = list()
"""