n = int(input())
e = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
visited = [0] * (n + 1)


def dfs(v):
    visited[v] = 1
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)


dfs(1)
print(sum(visited) - 1)
