from collections import deque

n, k = map(int, input().split())
graph = [-1] * 100001
graph[n] = 0
path = [0] * 100001
queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x == k:
        print(graph[x])
        result = []
        now = x
        for i in range(graph[x]+1):
            result.append(now)
            now = path[now]
        print(' '.join(map(str, reversed(result))))
        break

    for nx in (2 * x, x + 1, x - 1):
        if 0 <= nx <= 100000 and graph[nx] == -1:
            graph[nx] = graph[x] + 1
            queue.append(nx)
            path[nx] = x
