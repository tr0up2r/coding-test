from collections import deque


df = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]


def bfs(f, r, c):
    queue = deque([(f, r, c)])

    while queue:
        f, r, c = queue.popleft()
        for i in range(6):
            nf, nr, nc = f+df[i], r+dr[i], c+dc[i]
            if 0 <= nf < l and 0 <= nr < R and 0 <= nc < C and building[nf][nr][nc] != '#' and not data[nf][nr][nc]:
                data[nf][nr][nc] = data[f][r][c] + 1
                queue.append((nf, nr, nc))


while True:
    l, R, C = map(int, input().split())
    if not (l or R or C):
        break

    data = [[[0] * C for _ in range(R)] for _ in range(l)]
    building = []
    for _ in range(l):
        floor = []
        for _ in range(R):
            floor.append(list(input()))
        building.append(floor)
        input()

    for f in range(l):
        for r in range(R):
            for c in range(C):
                if building[f][r][c] == 'S':
                    bfs(f, r, c)
                    break

    for f in range(l):
        for r in range(R):
            for c in range(C):
                if building[f][r][c] == 'E':
                    if data[f][r][c]:
                        print(f"Escaped in {data[f][r][c]} minute(s).")
                    else:
                        print("Trapped!")
