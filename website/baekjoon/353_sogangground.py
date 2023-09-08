n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[1e9]*n for _ in range(n)]
for _ in range(r):
    a, b, w = map(int, input().split())
    graph[a-1][b-1] = w
    graph[b-1][a-1] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or k == j:
                continue
            if graph[i][k] and graph[k][j]:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

max_i = 0
for i in range(n):
    now_i = items[i]
    for j in range(n):
        if i != j and graph[i][j] <= m:
            now_i += items[j]
    max_i = max(max_i, now_i)

print(max_i)
