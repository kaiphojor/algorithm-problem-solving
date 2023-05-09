# 알고리즘은 쫀쫀하게 짜야한다...
# 예외처리 else 안붙여서 개고생한 경우...
import sys
input = sys.stdin.readline
input_str = input().strip()
bracket = ['(',')','[',']']
bracket_pair = {')':'(',']':'['}
bracket_point = {')':2,']':3}
def solve_bracket_equation(equation):
    stack = []
    for i,s in enumerate(equation):
        # ] ) 를 만나면 [ ( 를 만날때까지 pop
        if s in bracket_pair.keys():
            if i == 0:
                return 0
            number_stack = []
            while stack:
                last = stack.pop()
                # 여는 괄호를 만나기 전까지의 숫자를 모두 합산, 곱에 반영
                if last.isnumeric():
                    number_stack.append(int(last))
                elif bracket_pair[s] == last:
                    num_sum = 1
                    if number_stack:
                        num_sum = sum(number_stack)
                    cur_total = num_sum * bracket_point[s]
                    stack.append(str(cur_total))
                    break
                else:
                    return 0
                # 짝이 맞지 않을 경우 0 반환
                if not stack :
                    return 0
        elif s in bracket or s.isnumeric():
            stack.append(s)
        else:
            return 0
    if len(list(filter(lambda s: s in bracket, stack))) > 0:
        return 0;    
    return sum(map(int,stack))
print(solve_bracket_equation(input_str))