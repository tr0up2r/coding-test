R, C = map(int, input().split())
arr = [list(map(lambda x: ord(x)-ord('A'), input())) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
alpha = [False] * 26


def dfs(r, c, count):
    global max_count
    max_count = max(count, max_count)

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]

        if 0 <= nr < R and 0 <= nc < C and not alpha[arr[nr][nc]]:
            alpha[arr[nr][nc]] = True
            dfs(nr, nc, count+1)
            alpha[arr[nr][nc]] = False


max_count = 1
alpha[arr[0][0]] = True
dfs(0, 0, max_count)
print(max_count)
