a, b = map(int, input().split())
min_count = 1e9


def dfs(now, count):
    global min_count
    if now > b:
        return
    if now == b:
        min_count = min(min_count, count)
    now *= 2
    count += 1
    dfs(now, count)
    count -= 1
    now //= 2

    now = now * 10 + 1
    count += 1
    dfs(now, count)
    now = (now - 1) // 10
    count -= 1


dfs(a, 0)
print(-1 if min_count == 1e9 else min_count+1)
