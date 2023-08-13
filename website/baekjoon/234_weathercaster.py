h, w = map(int, input().split())
sky = [list(input()) for _ in range(h)]
answer = [[-1] * w for _ in range(h)]
now = []

for r in range(h):
    for c in range(w):
        if sky[r][c] == 'c':
            answer[r][c] = 0
            now.append((r, c))

for r, c in now:
    while 0 <= c+1 < w:
        if answer[r][c+1] != 0:
            answer[r][c+1] = answer[r][c] + 1
        c += 1

for r in answer:
    for v in r:
        print(v, end=' ')
    print()
    