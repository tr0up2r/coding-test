arr = [list(input().split()) for _ in range(5)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
s = set()


def dfs(r, c, now):
    if len(now) == 6:
        s.add(now)
        return

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, now+arr[nr][nc])


for r in range(5):
    for c in range(5):
        dfs(r, c, arr[r][c])
print(len(s))
