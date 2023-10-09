n, m = map(int, input().split())
arr = list(range(1, n+1))


def dfs(now):
    if len(now) == m:
        print(*now)
        return

    for num in arr:
        if num not in now:
            now.append(num)
            dfs(now)
            now.pop()


dfs([])
