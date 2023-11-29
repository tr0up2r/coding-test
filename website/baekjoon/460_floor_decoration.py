n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
answer = 0
drc = [[0, 1], [1, 0]]
for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            answer += 1
            for i, f in enumerate(('-', '|')):
                if arr[r][c] == f:
                    nr, nc = r, c
                    while True:
                        nr, nc = nr+drc[i][0], nc+drc[i][1]
                        if nr < n and nc < m and arr[nr][nc] == f:
                            visited[nr][nc] = True
                        else:
                            break
                    break
print(answer)
