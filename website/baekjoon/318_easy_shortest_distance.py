from collections import deque


n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
arr = [[0]*m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(n):
    for c in range(m):
        if data[r][c] == 2:
            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0 <= nr < n and 0 <= nc < m and not arr[nr][nc] and data[nr][nc] == 1:
                        arr[nr][nc] = arr[r][c] + 1
                        queue.append((nr, nc))
            break

for r in range(n):
    for c in range(m):
        if data[r][c] == 1 and arr[r][c] == 0:
            print(-1, end=' ')
        else:
            print(arr[r][c], end=' ')
    print()
