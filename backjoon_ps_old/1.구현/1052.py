N, K = map(int,input().split())
bottle_sum = 0 
reversed_binary_n = "".join(reversed(bin(N)))[:-2]
while reversed_binary_n.count('1') > K:
    new_str = ""
    for i,c in enumerate(reversed_binary_n):
        if c == '1':
            bottle_sum += 2 ** i
            while reversed_binary_n[i] == '1':
                new_str += '0'
                i += 1
                if i >= len(reversed_binary_n):
                    break
            new_str += '1'
            if i+1 < len(reversed_binary_n):                
                reversed_binary_n = new_str + reversed_binary_n[i+1:]
            else:
                reversed_binary_n = new_str
            break
        else:
            new_str += '0'
print(bottle_sum)
"""
남이 푼 답. 더 간결하다
N, K = map(int, input().split())

purchased_water_bottle_cnt = 0

while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    purchased_water_bottle_cnt += 2**idx
    N += 2**idx

print(purchased_water_bottle_cnt)
"""