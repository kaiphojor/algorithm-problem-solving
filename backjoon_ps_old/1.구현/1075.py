N = int(input())
F = int(input())
remainder = N % 100
remainder_removed = N - remainder
for r in range(100):
    if (remainder_removed + r) % F == 0:
        print(str(r).zfill(2))
        break
