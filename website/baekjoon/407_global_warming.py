n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

gone = []
min_r, max_r, min_c, max_c = 1e9, -1e9, 1e9, -1e9
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'X':
            count = 0
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 'X':
                    count += 1
            if count >= 2:
                min_r, max_r, min_c, max_c = min(min_r, r), max(max_r, r), min(min_c, c), max(max_c, c)
            else:
                gone.append((r, c))
for r, c in gone:
    arr[r][c] = '.'

for r in range(min_r, max_r+1):
    for c in range(min_c, max_c+1):
        print(arr[r][c], end='')
    print()
