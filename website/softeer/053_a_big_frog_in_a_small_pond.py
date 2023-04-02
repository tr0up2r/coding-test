import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weight = [0]
graph = [[] for _ in range(n+1)]

# 1번 인덱스에 1번 사람의 무게가 저장
weight.extend(list(map(int, input().split())))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1, n+1):
    am_i_greatest = True
    for node in graph[i]:
        if weight[i] <= weight[node]:
            am_i_greatest = False
            break
    if am_i_greatest:
        result += 1

print(result)
