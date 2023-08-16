import heapq as hq
import sys


n = int(sys.stdin.readline())
data = []

for _ in range(n):
    op = int(sys.stdin.readline())
    if op == 0:
        if not data:
            print(0)
        else:
            print(hq.heappop(data))
    else:
        hq.heappush(data, op)
