'''
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.
'''
def solution(n):
    return "".join(['수' if i%2 == 0 else '박' for i in range(n)])
# 다른 사람의 더 잘 푼 풀이 
def water_melon(n):
    s = "수박" * n
    return s[:n]

# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
def solution(s):
    return -int(s[1:]) if s[0] == '-' else int(s)
# 다른 사람의 잘 푼 풀이
def strToInt(str):
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result

'''
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
'''
def solution(a, b):
    answer = 0
    for i,v in enumerate(a):
        answer += a[i] * b[i]
    return answer
# 더 잘 푼 풀이
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])


'''
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
'''
def solution(s, n):
    answer = ''
    for i in s :    
        if chr(ord(i.lower()) + n) > 'z':
            answer += chr(ord(i)-26 + n)
        elif i == ' ':
            answer += i
        else :
            answer += chr(ord(i) +n)            
    return answer
# 다른 사람의 잘 푼 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

