R, C, k = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(input()))

goal = (0, C-1)
visited = [[0]*C for _ in range(R)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = 0


def dfs(r, c, count):
    if (r, c) == goal:
        if count == k:
            global answer
            answer += 1
        return

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and arr[nr][nc] != 'T':
            visited[nr][nc] = 1
            dfs(nr, nc, count+1)
            visited[nr][nc] = 0


visited[R-1][0] = 1
dfs(R-1, 0, 1)
print(answer)
