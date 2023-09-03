import sys
from heapq import heappop, heappush


n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
