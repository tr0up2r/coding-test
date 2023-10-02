from collections import deque


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque()
for r in range(n):
    for c in range(n):
        if arr[r][c]:
            queue.append((arr[r][c], r, c))
while s:
    queue = deque(sorted(queue, key=lambda q: q[0]))
    now_len = len(queue)
    while now_len:
        v, r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not arr[nr][nc]:
                arr[nr][nc] = v
                queue.append((v, nr, nc))
        now_len -= 1
    s -= 1

print(arr[x-1][y-1])
