n, m = map(int, input().split())
arr = list(range(1, n+1))


def dfs(now):
    if len(now) == m:
        print(*now)
        return

    for i in arr:
        if now[-1] <= i:
            now.append(i)
            dfs(now)
            now.pop()


for i in arr:
    dfs([i])
