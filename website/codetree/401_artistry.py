from collections import deque


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, v, group):
    global visited
    count = 1
    queue = deque([(r, c)])
    rcs = set()
    while queue:
        r, c = queue.popleft()
        rcs.add((r, c))
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if arr[nr][nc] == v:
                    visited[nr][nc] = True
                    groups[nr][nc] = group
                    queue.append((nr, nc))
                    count += 1
    return [count, v, rcs]


def get_score(g1, g2, d, count):
    return (d[g1][0]+d[g2][0])*d[g1][1]*d[g2][1]*count


def rotate(arr):
    new = [[0]*n for _ in range(n)]

    # 십자 모양 반시계 회전
    c = n//2
    for r in range(n):
        new[n-c-1][r] = arr[r][c]
    r = n//2
    for c in range(n):
        new[n-c-1][r] = arr[r][c]

    # 4개 정사각형 시계 방향 회전
    srs, scs = [0, n//2+1], [0, n//2+1]
    for sr in srs:
        for sc in scs:
            tmp, now = [[0]*(n//2) for _ in range(n//2)], []
            for a in arr[sr:sr+n//2]:
                now.append(a[sc:sc+n//2])
            for r in range(n//2):
                for c in range(n//2):
                    tmp[c][(n//2)-r-1] = now[r][c]
            for r in range(sr, sr+n//2):
                for c in range(sc, sc+n//2):
                    new[r][c] = tmp[r-sr][c-sc]

    return new


answer = 0
for _ in range(4):
    visited = [[False] * n for _ in range(n)]
    groups = [[0] * n for _ in range(n)]
    # 1. 그룹 만들기
    group = 1
    d = dict()
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                visited[r][c] = True
                groups[r][c] = group
                d[group] = bfs(r, c, arr[r][c], group)
                group += 1

    # 2. 예술성 계산
    score = 0
    for g1 in range(1, group-1):
        for g2 in range(g1+1, group):
            count = 0
            if g1 != g2:
                for r, c in d[g1][2]:
                    for i in range(4):
                        nr, nc = r+dr[i], c+dc[i]
                        if 0 <= nr < n and 0 <= nc < n:
                            if (nr, nc) in d[g2][2]:
                                count += 1
                if count:
                    score += get_score(g1, g2, d, count)
    answer += score

    # 3. 배열 회전
    arr = rotate(arr)

print(answer)
