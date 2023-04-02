import sys
import heapq
input = sys.stdin.readline

w, n = map(int, input().split())
h = []
price = 0

for _ in range(n):
    # m: 무게, p: 무게 당 가격
    m, p = map(int, input().split())
    heapq.heappush(h, (-p, m))

while True:
    now = heapq.heappop(h)
    now_p = -now[0]
    now_m = now[1]
    if now_m < w:
        price += now_p * now_m
        w -= now_m
    else:
        price += now_p * w
        break

print(price)
