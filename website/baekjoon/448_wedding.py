n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
s = set()


def dfs(now, depth):
    if not graph[now] or depth > 2:
        return
    for x in graph[now]:
        if x != 1:
            s.add(x)
            dfs(x, depth+1)


dfs(1, 1)
print(len(s))
