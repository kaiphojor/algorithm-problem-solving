'''
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
'''
def solution(arr, divisor):
    answer = []
    # 나눠지는 경우에만 답변에 포함
    answer = [i for i in arr if i % divisor == 0]
    # 오름차순 정렬
    answer.sort()
    # 나눠지는 요소가 없을 경우
    if len(answer) == 0 :
        answer = [-1]
    return answer

# 다른 사람들의 참신한 답변
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]