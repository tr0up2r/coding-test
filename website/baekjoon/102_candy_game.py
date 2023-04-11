n = int(input())
data = []
for _ in range(n):
    data.append(list(list(input())))

max_count = 1


def candy_count():
    global max_count
    for i in range(n):
        count = 1
        for j in range(1, n):
            if data[i][j] == data[i][j - 1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)

        count = 1
        for j in range(1, n):
            if data[j][i] == data[j-1][i]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)


# 우 하
dx = [0, 1]
dy = [1, 0]

candy_count()
for i in range(n):
    for j in range(n):
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= n or ny >= n:
                continue
            if data[i][j] == data[nx][ny]:
                continue

            data[i][j], data[nx][ny] = data[nx][ny], data[i][j]
            candy_count()
            data[i][j], data[nx][ny] = data[nx][ny], data[i][j]

print(max_count)
