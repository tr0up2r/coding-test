from collections import deque


n = int(input())
data = [[] for _ in range(n)]

a, b = map(int, input().split())
a -= 1
b -= 1
m = int(input())

for _ in range(m):
    start, end = map(int, input().split())
    data[start-1].append(end-1)
    data[end-1].append(start-1)


def bfs():
    queue = deque([(a, -1)])
    visited = [False] * n
    while queue:
        now, count = queue.popleft()
        count += 1
        if now == b:
            return count
        if not data[now]:
            return -1
        visited[now] = True
        for node in data[now]:
            if not visited[node]:
                queue.append((node, count))
    return -1


print(bfs())
