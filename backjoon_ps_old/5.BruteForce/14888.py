from itertools import permutations
N = int(input())
seq = list(map(int,input().split()))
op_count = list(map(int,input().split()))
ops= []
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if a < 0:
        return -((-a) // b)
    return a // b
def get_result(op):
    result = seq[0]
    for i in range(N-1):
        result = operation[op[i]](result,seq[i+1])
    return result
operation = [add,sub,mult,div]
for i in range(4):
    ops.extend([i] * op_count[i])
op_result = list(map(get_result,list(set(permutations(ops)))))
print(max(op_result))
print(min(op_result))
