n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1], arr[b-1][a-1] = 1, 1

# Floyd-Warshall 풀이
for k in range(n):
    for i in range(n):
        for j in range(n):
            if k == j:
                continue
            if arr[i][k] and arr[k][j]:
                if arr[i][j] == 0:
                    arr[i][j] = arr[i][k]+arr[k][j]
                else:
                    arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

min_i = 0
min_s = 1e9
for i in range(n):
    now_s = sum(arr[i])
    if now_s < min_s:
        min_i, min_s = i, now_s

print(min_i+1)


# bfs 풀이
# from collections import deque


# answer = [[0]*n for _ in range(n)]
#
#
# def bfs(x):
#     queue = deque([(x, 0)])
#     check = [0 for _ in range(n)]
#
#     while queue:
#         q, count = queue.popleft()
#         for i in range(n):
#             if i != x and not check[i] and arr[q][i] and not answer[x][i]:
#                 answer[x][i] = count+1
#                 check[i] = 1
#                 queue.append((i, count+1))
#
#
# min_i = 0
# min_s = 1e9
# for i in range(n):
#     bfs(i)
#     now_s = sum(answer[i])
#     if now_s < min_s:
#         min_i, min_s = i, now_s
#
# print(min_i+1)
