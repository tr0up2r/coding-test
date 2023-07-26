def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    dx = [0, 1, 1]
    dy = [1, 0, 1]

    while True:
        four = []
        for i in range(m - 1):
            for j in range(n - 1):
                if not board[i][j].isalpha():
                    continue

                temp = [(i, j)]

                for k in range(3):
                    nx, ny = i + dx[k], j + dy[k]
                    if board[i][j] != board[nx][ny]:
                        break
                    temp.append((nx, ny))

                if len(temp) == 4:
                    four.extend(temp)

        four = set(four)

        if not four:
            break

        for x, y in four:
            board[x][y] = '0'
            answer += 1

        for i in range(m - 1, -1, -1):
            for j in range(n):
                if board[i][j] == '0':
                    x = -1
                    while i + x >= 0:
                        nx = i + x
                        if board[nx][j] != '0':
                            board[i][j], board[nx][j] = board[nx][j], '0'
                            break
                        x -= 1

    return answer
