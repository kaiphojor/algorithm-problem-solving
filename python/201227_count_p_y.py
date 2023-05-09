'''
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
'''
def solution(s):
    answer = True
    s = s.lower()
    py_arr = [0,0]
    for c in s :
        if c == 'p':
            py_arr[0] += 1 
        elif c == 'y':
            py_arr[1] += 1       
    return py_arr[0] == py_arr[1]
# 잘 푼 사람의 예시
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')