n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
min_count = 1e9

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for sr in range(n-7):
    for sc in range(m-7):
        b_count, w_count = 0, 0
        for r in range(sr, sr+8):
            for c in range(sc, sc+8):
                if (r + c) % 2:
                    if arr[r][c] == 'B':
                        b_count += 1
                    else:
                        w_count += 1
                else:
                    if arr[r][c] == 'B':
                        w_count += 1
                    else:
                        b_count += 1
        min_count = min(min_count, w_count, b_count)

print(min_count)
