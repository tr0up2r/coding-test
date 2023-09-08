from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distance = [0] * (n + 1)
    distance[1] = 1

    queue = deque([1])
    while queue:
        now = queue.popleft()
        for v in graph[now]:
            if not distance[v]:
                distance[v] = distance[now] + 1
                queue.append(v)

    max_v = max(distance[1:])
    for d in distance:
        if d == max_v:
            answer += 1

    return answer
