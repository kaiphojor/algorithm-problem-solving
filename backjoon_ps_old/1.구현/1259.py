def is_palindrome(num_str):
    N = len(num_str)
    front = 0
    rear = N-1
    while front <= rear:
        if num_str[front] != num_str[rear]:
            return False
        front += 1 
        rear -= 1
    return True
result = []
while True:
    input_str = input()
    if int(input_str) == 0:
        break
    if(is_palindrome(input_str)):
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)