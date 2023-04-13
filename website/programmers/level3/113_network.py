from collections import deque


def solution(n, computers):
    def bfs(i):
        queue = deque()
        queue.append(i)
        while queue:
            i = queue.popleft()
            visited[i] = True
            for j in range(n):
                if computers[i][j] and not visited[j]:
                    queue.append(j)

    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1

    return count
