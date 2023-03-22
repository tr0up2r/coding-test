import sys

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

input = sys.stdin.readline  # 빠른 입력을 위한 input 함수 재정의
INF = int(1e9)

n, m = map(int, input().split())  # n: 노드 수, m: 간선 수
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())  # a 노드에서 b 노드로 가는 비용 c
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        # (graph[start]에서 갈 수 있는 노드, 비용) tuple들을 꺼내기
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()  # 현재 최단 거리가 가장 짧은 노드 꺼내기
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:  # 거쳐 가는 거리가 더 짧은 경우
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")  # 도달할 수 없는 경우
    else:
        print(distance[i])
