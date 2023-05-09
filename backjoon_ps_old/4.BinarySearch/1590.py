import sys
input = sys.stdin.readline
N, T = map(int, input().split())

result = 2 ** 31 - 1
for _ in range(N):
    bus_start_time, interval, bus_count = map(int, input().split())
    base_time = T - bus_start_time
    if base_time <= (last_arrival := interval * (bus_count-1)):
        start, end = 0, bus_count - 1
        eta = last_arrival - base_time

        while start <= end:
            mid = (start + end) // 2
            if (cur_eta := mid * interval - base_time) >= 0:
                eta = min(eta,cur_eta)
                end = mid - 1
            else:
                start = mid + 1

        result = min(result,eta)

print(result if result != 2 ** 31 - 1 and result >= 0 else -1)