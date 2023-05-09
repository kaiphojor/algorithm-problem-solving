'''
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.
'''
def solution(strings, n):
    # 인덱스 기준으로 자르고 정렬
    strings = sorted(strings)
    answer = sorted([i[n:] for i in strings])
    # 정렬된 배열의 잘린 부분을 복원
    for i,v in enumerate(answer) : 
        for string in strings : 
            if string[n:] == v : 
                answer[i] = string 
                strings.remove(string)
                print(strings)
                break
    # index의 문자가 같은 문자열들을 사전순 정렬
    buffer=[]
    start_chr = 'a'
    for i in range(ord('z')-(ord('a')-1)):
        idx_chr = chr(ord(start_chr)+i)
        chr_arr = sorted([i for i in answer if i[n] == idx_chr])
        buffer += chr_arr
    answer = buffer
    return answer

# 다른 사람의 더 잘 푼 예제
def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings