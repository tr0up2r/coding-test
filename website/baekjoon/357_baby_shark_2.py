from collections import deque


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
queue = deque()

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs():
    while queue:
        r, c = queue.popleft()
        for i in range(8):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and not arr[nr][nc]:
                arr[nr][nc] = arr[r][c]+1
                queue.append((nr, nc))


for r in range(n):
    for c in range(m):
        if arr[r][c]:
            queue.append((r, c))
bfs()

print(max(map(max, arr))-1)
