import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

cnt = []


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        cnt.append(1)
        graph[x][y] = 0

        # 상 하 좌 우 탐색
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0
result_list = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            result_list.append(len(cnt))
            cnt = []

print(result)
result_list.sort()
for c in result_list:
    print(c)
