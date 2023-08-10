from collections import deque


def solution(n, wires):
    answer = 1e9
    wires = [[i - 1, j - 1] for i, j in wires]

    for i in range(len(wires)):
        visited = [0] * n
        tree = [[] for _ in range(n)]

        for j in range(len(wires)):
            if j == i:
                continue
            start, end = wires[j]
            tree[start].append(end)
            tree[end].append(start)

        queue = deque([0])
        while queue:
            now = queue.popleft()
            if not tree[now]:
                break
            for node in tree[now]:
                if not visited[node]:
                    visited[node] = 1
                    queue.append(node)

        answer = min(answer, abs(visited.count(0) - visited.count(1)))

    return answer
