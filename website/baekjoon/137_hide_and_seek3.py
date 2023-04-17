from collections import deque

n, k = map(int, input().split())
graph = [-1] * 100001
graph[n] = 0
queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    for nx in (2 * x, x + 1, x - 1):
        if 0 <= nx <= 100000 and graph[nx] == -1:
            if nx == 2 * x:
                graph[nx] = graph[x]
                queue.appendleft(nx)
            else:
                graph[nx] = graph[x] + 1
                queue.append(nx)

print(graph[k])
