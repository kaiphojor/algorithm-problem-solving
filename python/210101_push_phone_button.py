'''
이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
'''

def solution(numbers, hand):
    answer = ''
    # 반드시 왼/오른쪽으로 눌러야 하는 것
    left = [1,4,7]
    right = [3,6,9]
    # 튜플 좌표 계산 함수 - 좌상단부터 0,0
    def get_coordinate(num) :
        cur_x = 3 if num == 0 else (num+2)//3-1
        cur_y = 1 if num == 0 else (num-1)% 3 
        return (cur_x,cur_y)
    # 절대값 적용한 manhattan distance
    def get_absolute(coordinate):
        x,y = coordinate
        if x < 0 :
            x = -x
        if y < 0 : 
            y = -y
        return x+y
    # *, # 의 좌표
    cur_left = (3,0)
    cur_right = (3,2)
    
    for n in numbers :
        n_coordinate = get_coordinate(n)
        # 동일한 좌표 or 양측 번호 일시
        if n in left or cur_left == n_coordinate:
            answer += 'L'
            cur_left = n_coordinate
        elif n in right or cur_right == n_coordinate:
            answer += 'R'
            cur_right = n_coordinate           
        else :
            # 목표로 누르려는 번호 좌표와의 차이 구해서 비교
            dist_left_raw = (cur_left[0] - n_coordinate[0],cur_left[1]-n_coordinate[1]) 
            dist_left = get_absolute(dist_left_raw)
            dist_right_raw = (cur_right[0] - n_coordinate[0],cur_right[1]-n_coordinate[1]) 
            dist_right = get_absolute(dist_right_raw)
            if dist_left < dist_right :
                answer += 'L'
                cur_left = n_coordinate
            elif dist_right < dist_left : 
                answer += 'R'
                cur_right = n_coordinate  
            elif hand == 'left':
                answer += 'L'
                cur_left = n_coordinate
            elif hand == 'right':                
                answer += 'R'
                cur_right = n_coordinate    
    return answer




# 다른사람의 풀이 
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

'''
정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.
'''
def solution(num):
    return 'Even' if num%2==0 else 'Odd'
# 다른 사람의 풀이
def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"