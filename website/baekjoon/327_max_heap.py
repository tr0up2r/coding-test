import sys
from heapq import heappop, heappush


n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heappush(heap, -x)
    else:
        print(-heappop(heap) if heap else 0)
