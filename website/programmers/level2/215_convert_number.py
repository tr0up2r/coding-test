from collections import deque


def bfs(x, y, n):
    data = [-1] * 1000001
    ops = [n, 2, 3]

    queue = deque()
    data[x] = 0
    queue.append(x)

    while queue:
        x = queue.popleft()
        for i in range(len(ops)):
            if i == 0:
                nx = x + ops[i]
            else:
                nx = x * ops[i]
            if 0 <= nx <= 1000000 and data[nx] == -1:
                data[nx] = data[x] + 1
                queue.append(nx)
        if data[y] != -1:
            return data[y]
    return data[y]


def solution(x, y, n):
    return bfs(x, y, n)
