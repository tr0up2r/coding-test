n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0]*n


def dfs(now):
    if len(now) == m:
        print(*now)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            now.append(arr[i])
            dfs(now)
            now.pop()
            visited[i] = 0


dfs([])
