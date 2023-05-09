'''
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
'''
def solution(n):
    answer = n    
    for i in range(1,int(n//2)+1):
        if n % i == 0:
            answer += i
    return answer

# 다른사람 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

'''
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
'''
def solution(s):
    answer = ''
    is_odd = True
    for i in s :
        if i == ' ':
            is_odd = True
            answer += ' '
        elif is_odd :
            is_odd = False
            answer += i.upper()
        else :
            is_odd = True
            answer += i.lower()
    return answer

'''
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
'''
def solution(n):
    return sum(int(i) for i in str(n))

'''
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
'''
def solution(n):
    return list(map(int,str(n)[::-1]))


'''
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.
'''
def solution(n):
    return int("".join(map(str,sorted([int(i) for i in str(n)],reverse=True))))

# 다른 사람 풀이
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)));
