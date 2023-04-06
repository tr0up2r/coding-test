n, m, x, y, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
command = list(map(int, input().split()))

# 위 우 아래 왼 뒤 앞
dice = {'top': 0, 'right': 0, 'bottom': 0, 'left': 0, 'back': 0, 'front': 0}
dice_idx = (x, y)

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for c in command:
    nx = dice_idx[0]+dx[c-1]
    ny = dice_idx[1]+dy[c-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 지도 밖으로 이동시키려 할 때
        continue

    dice_idx = (nx, ny)
    if c == 1 or c == 2:
        if c == 1:  # 동쪽 이동
            dice['top'], dice['right'], dice['bottom'], dice['left'] = dice['left'], dice['top'], dice['right'], dice['bottom']
        else:  # 서쪽 이동
            dice['top'], dice['right'], dice['bottom'], dice['left'] = dice['right'], dice['bottom'], dice['left'], dice['top']
    else:
        if c == 3:  # 북쪽 이동
            dice['top'], dice['back'], dice['bottom'], dice['front'] = dice['front'], dice['top'], dice['back'], dice['bottom']
        else:  # 남쪽 이동
            dice['top'], dice['back'], dice['bottom'], dice['front'] = dice['back'], dice['bottom'], dice['front'], dice['top']

    if data[nx][ny] == 0:  # 이동한 칸이 0이면, 주사위 바닥면 수가 복사
        data[nx][ny] = dice['bottom']
    else:
        dice['bottom'] = data[nx][ny]
        data[nx][ny] = 0

    print(dice['top'])
