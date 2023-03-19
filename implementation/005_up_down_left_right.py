# 공간의 크기를 나타내는 N (N * N)
# L: 왼쪽으로 한 칸 이동, R: 오른족으로 한 칸 이동, U: 위로 한 칸 이동, D: 아래로 한 칸 이동
# 초기 위치: (1, 1)

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
