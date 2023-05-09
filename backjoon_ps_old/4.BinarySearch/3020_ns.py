"""
석순 종유석 번갈아서 -> 종유석 끝 
길이는 항상 짝수
1 1 H - n번째 구간 
석순 - 홀수 번째
    통과여부 H-1 개의 구간
    n <= 석순 O
    1 = 1
    2 = 2 
    H = 해당없음
종유석 짝수번째 
    통과여부 H-1개의 구간
    H+1 - n <= 종유석 = O 
    1 = 해당 없음 
    2 = H -1
    3 = H - 2
최소값 -> 뚫은 합의 최소값 
최소값을 구하고 최소값에 해당하는 구간 갯수 구하기
누적합 만들기

받고 정렬
높이 구간 하나 설정
1 ~ H  
통과하는 최소
구간 높이를 구한 다. 
구간 높이 최소높이에 해당하는 x 좌표를 구한다
    그 뒤로 싹다 ㅒ 
구간 높이를 구하고 
    최소 높이게 해당하는 x 좌표 
        싹다 구하기
    해당 구간에 대한 
mid <= jong
실패. pypy3
https://hongcoding.tistory.com/6
"""
N, H = map(int, input().split())
stalagmite = [0] * (H + 1 )
stalactite = [0] * (H + 1 )

min_count = N
range_count = 0

for i in range(N//2):
    stalagmite[int(input())] += 1
    stalactite[int(input())] += 1

for i in range(H-1,0,-1):
    stalagmite[i] += stalagmite[i+1]
    stalactite[i] += stalactite[i+1]

for i in range(1, H+1):
    if min_count > (stalagmite[i] + stalactite[H-i + 1]):
        min_count = (stalagmite[i] + stalactite[H-i + 1])
        range_count = 1
    elif min_count == (stalagmite[i] + stalactite[H-i + 1]):
        range_count += 1

print(min_count, range_count)
    
