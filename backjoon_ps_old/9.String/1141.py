N = int(input())
word_list = sorted([input() for _ in range(N)],key=len,reverse=True)
prefix_free_list = list()

def is_prefix(a,no_prefix_list):
    for b in no_prefix_list:
        if a == b[:len(a)]:
            return True
    return False
for word in word_list:
    if not prefix_free_list:
        prefix_free_list.append(word)
    elif not is_prefix(word,prefix_free_list):
        prefix_free_list.append(word)
print(len(prefix_free_list))
"""
긴 순으로 정렬
긴것들을 추가
    list에 인자 없으면 추가
    있다면 추가할 단어가 이미 추가된 단어의 접두사인지 확인한후 아니면 추가
"""