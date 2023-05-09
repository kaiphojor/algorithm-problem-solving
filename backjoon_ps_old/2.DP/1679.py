"""
둘이서 게임 
주어진 숫자를 정해진 숫자 만큼 사용(적을수도 있다) 하여 합을 구하는 것 
번갈아가면서
누가 이기는지 판별
"""
import sys 
input = sys.stdin.readline
N = int(input()) 
n_list = sorted(list(map(int,input().split())))
K = int(input())

num = 0

def is_sum_possible(n, limit):
    if n == 0 :
        return True
    if limit == 0:
        return False
    if n < min(n_list) or n > max(n_list) * limit:
        return False
    if n in n_list:
        return True
    for i in n_list:
        if i > n:
            continue 
        elif is_sum_possible(n-i,limit-1):
            return True
    return False

while True:
    num += 1
    if not is_sum_possible(num, K):
        if num % 2 == 0:
            print("holsoon win at %d" % num)
        else :
            print("jjaksoon win at %d" % num)
        break
