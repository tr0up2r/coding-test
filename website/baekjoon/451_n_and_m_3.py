m, n = map(int, input().split())


def dfs(now):
    if len(now) == n:
        print(*now)
        return
    for i in range(1, m+1):
        now.append(i)
        dfs(now)
        now.pop()


dfs([])
