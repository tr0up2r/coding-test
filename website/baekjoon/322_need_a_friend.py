from collections import deque


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

count = 0
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'I':
            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0 <= nr < n and 0 <= nc < m:
                        if arr[nr][nc] == 'X':
                            continue
                        if arr[nr][nc] == 'P':
                            count += 1
                        arr[nr][nc] = 'X'
                        queue.append((nr, nc))
            break

if count:
    print(count)
else:
    print('TT')
