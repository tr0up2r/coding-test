from collections import deque


M, N, H = map(int, input().split())
arr = []
for _ in range(H):
    now = []
    for _ in range(N):
        now.append(list(map(int, input().split())))
    arr.append(now)
dh = [0, 0, 0, 0, -1, 1]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

queue = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 1:
                queue.append((h, r, c))

while queue:
    h, r, c = queue.popleft()
    visited[h][r][c] = 1
    for i in range(6):
        nh, nr, nc = h + dh[i], r + dr[i], c + dc[i]
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0 and not visited[nh][nr][nc]:
            arr[nh][nr][nc] = arr[h][r][c] + 1
            queue.append((nh, nr, nc))

answer = -1
flag = False
for h in range(H):
    for r in range(N):
        for c in range(M):
            if flag:
                break
            if arr[h][r][c] == 0:
                answer = -1
                flag = True
                break
            if arr[h][r][c] != -1:
                answer = max(answer, arr[h][r][c]-1)
print(answer)
