n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
cam = []
area = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            area += 1
        if 1 <= arr[i][j] <= 5:
            cam.append((arr[i][j], i, j))

# 1, 2, 3, 4, 5 cam
dt = [[0], [0, 2], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
answer = 1e9


def dfs(idx, now):
    if len(now) == len(cam):
        count = 0
        visited = [[0]*m for _ in range(n)]
        for t, c in now:
            now_dr = list(map(lambda x: (x+t)%4, dt[c[0]-1]))
            for d in now_dr:
                nr, nc = c[1], c[2]
                while True:
                    nr, nc = nr+dr[d], nc+dc[d]
                    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 6:
                        if arr[nr][nc] == 0 and not visited[nr][nc]:
                            count += 1
                            visited[nr][nc] = 1
                        elif 1 <= arr[nr][nc] <= 5:
                            continue
                    else:
                        break

        global answer
        if area-count < answer:
            answer = min(answer, area-count)

        return

    for i in range(idx, len(cam)):
        if cam[i][0] == 2:
            turn = 2
        elif cam[i][0] == 5:
            turn = 1
        else:
            turn = 4
        for j in range(turn):
            now.append((j, cam[i]))
            dfs(i+1, now)
            now.pop()


dfs(0, [])
print(answer)
