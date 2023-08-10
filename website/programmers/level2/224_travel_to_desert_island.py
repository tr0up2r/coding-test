from collections import deque


def solution(maps):
    maps = list(map(list, maps))
    answer = []

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        res = 0

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while queue:
            r, c = queue.popleft()
            if maps[r][c] == 'X':
                continue
            res += int(maps[r][c])
            maps[r][c] = 'X'

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and maps[nr][nc] != 'X':
                    queue.append((nr, nc))
        return res

    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] != 'X':
                answer.append(bfs(r, c))

    return sorted(answer) if answer else [-1]
