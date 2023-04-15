from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001


def bfs(x):
    queue = deque()
    queue.append(x)
    graph = [0] * 100001
    visited[x] = True

    while queue:
        if graph[k] != 0:
            return graph[k]
        x = queue.popleft()
        for i in range(3):
            if i == 0:
                nx = x - 1
            elif i == 1:
                nx = x + 1
            else:
                nx = x * 2
            if nx < 0 or nx >= 100001 or visited[nx]:
                continue
            visited[nx] = True
            graph[nx] = graph[x] + 1
            queue.append(nx)
    return 0


print(bfs(n))
