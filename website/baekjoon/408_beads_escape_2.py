from collections import deque


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'R':
            rr, rc = r, c
        elif arr[r][c] == 'B':
            br, bc = r, c
        elif arr[r][c] == 'O':
            hole = (r, c)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque([(rr, rc, br, bc, 0)])
visited = set()
visited.add((rr, rc, br, bc))


def get_nrnc(r, c):
    j = 1
    while True:
        nr, nc = r+(dr[i]*j), c+(dc[i]*j)
        if 0 <= nr < n and 0 <= nc < m:
            if (nr, nc) == hole:
                return nr, nc
            elif arr[nr][nc] == '#':
                return r+(dr[i]*(j-1)), c+(dc[i]*(j-1))
            j += 1


answer = 1e9
while queue:
    rr, rc, br, bc, count = queue.popleft()
    if count >= 10:
        continue

    for i in range(4):
        nrr, nrc = get_nrnc(rr, rc)
        nbr, nbc = get_nrnc(br, bc)

        if (nrr, nrc, nbr, nbc) not in visited:
            if (nbr, nbc) == hole:
                continue
            elif (nrr, nrc) == hole:
                answer = min(answer, count+1)
                continue
            elif nrr == nbr and nrc == nbc:
                r_dist, b_dist = abs(nrr-rr)+abs(nrc-rc), abs(nbr-br)+abs(nbc-bc)
                if r_dist > b_dist:
                    nrr, nrc = nrr-dr[i], nrc-dc[i]
                else:
                    nbr, nbc = nbr-dr[i], nbc-dc[i]
            queue.append((nrr, nrc, nbr, nbc, count+1))
            visited.add((nrr, nrc, nbr, nbc))

print(answer if answer != 1e9 else -1)
