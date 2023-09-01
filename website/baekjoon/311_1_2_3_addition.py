t = int(input())


def dfs(now):
    global count
    if now == n:
        count += 1
        return

    for i in range(1, 4):
        now += i
        if now <= n:
            dfs(now)
        now -= i


for _ in range(t):
    n = int(input())
    count = 0
    dfs(0)
    print(count)
