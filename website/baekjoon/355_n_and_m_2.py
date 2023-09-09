n, m = map(int, input().split())


def dfs(now):
    if len(now) == m:
        print(*now)
        return

    for i in range(1, n+1):
        if not now or now[-1] < i:
            now.append(i)
            dfs(now)
            now.pop()


dfs([])
