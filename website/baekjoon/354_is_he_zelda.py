from heapq import heappush, heappop


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

count = 1
while True:
    n = int(input())
    if n == 0:
        break

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    money = [[1e9]*n for _ in range(n)]

    queue = []
    heappush(queue, (arr[0][0], 0, 0))
    money[0][0] = arr[0][0]
    while queue:
        now, r, c = heappop(queue)
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and now+arr[nr][nc] < money[nr][nc]:
                money[nr][nc] = now+arr[nr][nc]
                heappush(queue, (now+arr[nr][nc], nr, nc))

    print(f'Problem {count}: {money[n-1][n-1]}')
    count += 1
