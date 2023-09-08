from heapq import heappush, heappop


v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
distance = [1e9]*(v+1)


def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(queue, (cost, i[0]))


dijkstra(start)

for d in distance[1:]:
    print('INF' if d == 1e9 else d)
