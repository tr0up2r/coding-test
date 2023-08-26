from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        queue = deque([i])
        while queue:
            now = queue.popleft()
            if not graph[now]:
                break
            for node in graph[now]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
        count += 1

print(count)
