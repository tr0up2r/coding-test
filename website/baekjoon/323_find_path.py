from collections import deque


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0] * n for _ in range(n)]


def bfs(x):
    queue = deque([x])
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()
        for i in range(n):
            if not check[i] and graph[q][i]:
                check[i] = 1
                visited[x][i] = 1
                queue.append(i)


for i in range(n):
    bfs(i)

for v in visited:
    print(*v)
