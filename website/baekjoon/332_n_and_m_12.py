n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = set()


def dfs(now):
    if len(now) == m:
        now_s = ' '.join(list(map(str, now)))
        if now_s not in s:
            print(*now)
            s.add(now_s)
        return

    for i in arr:
        if now[-1] <= i:
            now.append(i)
            dfs(now)
            now.pop()


for i in arr:
    dfs([i])
