# 맵의 세로 크기 N, 가로 크기 M 입력
# 게임 캐릭터의 좌표, 방향 d가 공백으로 구분하여 주어짐.
# 셋째 줄부터 육지(0), 바다(1)로 이루어진 맵 정보가 주어짐. (맵의 외곽은 항상 바다)

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0

while True:
    direction = (direction-1) % 4  # -1 % 4 => 3
    nx = x + dx[direction]
    ny = y + dy[direction]

    if array[nx][ny] == 0 and d[nx][ny] == 0:
        x = nx
        y = ny
        d[nx][ny] = 1
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
