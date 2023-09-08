from heapq import heappush, heappop


n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    bus[a].append((b, w))
src, dst = map(int, input().split())
distance = [1e9]*(n+1)
distance[src] = 0

queue = []
heappush(queue, (0, src))
while queue:
    dist, now = heappop(queue)
    if distance[now] < dist:
        continue

    for i in bus[now]:
        cost = dist+i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            queue.append((cost, i[0]))

print(distance[dst])
