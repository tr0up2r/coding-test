from collections import deque


n, m = map(int, input().split())
s_and_l = [0]*101
for _ in range(n+m):
    src, dst = map(int, input().split())
    s_and_l[src] = dst

board = [1e9]*101
queue = deque([1])
board[1] = 0
while queue:
    x = queue.popleft()
    for d in range(1, 7):
        nx = x+d
        if nx <= 100:
            if s_and_l[nx]:
                nx = s_and_l[nx]
            if board[x]+1 < board[nx]:
                board[nx] = board[x]+1
                queue.append(nx)

print(board[100])
