'''
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
'''
import math
def solution(n):
    ans = [2]
    for i in range(3,n+1,2): 
        flag = True
        for j in range(3,int(math.sqrt(i)+1),2):          
            if i % j == 0:
                flag = False
                break
        if flag :
            ans.append(i)
    # print(ans)
    answer = len(ans)
    return answer

# 에라토스테네스의 체 - 다른 사람의 잘푼 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


'''
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
'''
def solution(s):
    s = list(s)
    s.sort(reverse=True)
    answer = "".join(s)
    return answer
# 잘푼사람의 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))

'''
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.
'''
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
# 잘푼사람의 풀이 
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

'''
String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
'''
def solution(seoul):
    return '김서방은 '+str(seoul.index('Kim'))+'에 있다'
# 잘푼 사람의 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))