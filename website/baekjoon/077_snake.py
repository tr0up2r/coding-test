n = int(input())  # 보드 크기
k = int(input())  # 사과 개수

data = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    data[x-1][y-1] = 2  # 사과
data[0][0] = 1  # 뱀
snake = [(0, 0)]

l = int(input())
command = []
for _ in range(l):
    x, c = input().split()
    command.append((int(x), c))

# 우 상 좌 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 처음엔 오른쪽 바라봄
now_d = 0


sec = 0
c = 0
while True:
    s = snake[len(snake)-1]
    nx = s[0]+dx[now_d]
    ny = s[1]+dy[now_d]
    sec += 1

    if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 벽에 부딪히면 끝
        break
    if data[nx][ny] == 1:  # 자신의 몸과 부딪히면 끝
        break
    if data[nx][ny] == 2:
        data[nx][ny] = 1  # 이동한 칸에 사과가 있다면 사과는 없어지고 꼬리는 움직이지 않는다
    else:  # 사과가 없다면
        data[nx][ny] = 1
        ox, oy = snake.pop(0)
        data[ox][oy] = 0
    snake.append((nx, ny))

    if c < len(command):
        if sec == command[c][0]:
            if command[c][1] == 'L':  # 왼쪽 회전
                now_d = (now_d+1)%4
            else:  # 오른쪽 회전
                now_d = (now_d-1)%4
            c += 1

print(sec)
