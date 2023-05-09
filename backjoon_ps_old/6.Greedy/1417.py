N = int(input())
candidates = list(map(int,[input() for _ in range(N)]))
count = 0
while True:
    if max(candidates) not in candidates[1:]:
        break
    selected = candidates.index(max(candidates),1)
    candidates[selected] -= 1
    candidates[0] += 1
    count += 1

print(count)