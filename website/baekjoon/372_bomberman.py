R, C, N = map(int, input().split())
bombs = [list(input()) for _ in range(R)]
arr = [[0]*C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if bombs[r][c] == 'O':
            arr[r][c] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

sec = 1
while sec < N:
    if sec % 2:
        for r in range(R):
            for c in range(C):
                if arr[r][c]:
                    arr[r][c] += 1
                else:
                    arr[r][c] = 1
    else:
        for r in range(R):
            for c in range(C):
                if arr[r][c] == 2:
                    arr[r][c] = 0
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != 2:
                            arr[nr][nc] = 0
    sec += 1

for r in range(R):
    for c in range(C):
        if arr[r][c]:
            print('O', end='')
        else:
            print('.', end='')
    print()
