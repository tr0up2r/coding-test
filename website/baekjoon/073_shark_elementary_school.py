n = int(input())
data = {}
for _ in range(n**2):
    line = list(map(int, input().split()))
    data[line[0]] = line[1:]
room = [[0] * n for _ in range(n)]

# 인접한 칸: 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 학생 배치
for student, like in zip(data.keys(), data.values()):
    like_count_list = []
    # 1. 좋아하는 학생이 인접한 칸에 가장 많은 칸
    for i in range(n):
        for j in range(n):
            if room[i][j] != 0:
                continue
            like_count = 0
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if room[nx][ny] in like:
                    like_count += 1
            like_count_list.append([like_count, (i, j)])

    max_like = -1e9
    for l in like_count_list:
        max_like = max(max_like, l[0])

    like_index_list = []
    for l in like_count_list:
        if max_like == l[0]:
            like_index_list.append(l[1])

    # 적절한 자리가 딱 한 자리 있으면 그 자리에 배치
    if len(like_index_list) == 1:
        room[like_index_list[0][0]][like_index_list[0][1]] = student
        continue

    # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중 비어있는 칸이 가장 많은 칸
    empty_count_list = []
    for idx in like_index_list:
        empty_count = 0
        for i in range(4):
            nx = idx[0] + dx[i]
            ny = idx[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if room[nx][ny] == 0:
                empty_count += 1
        empty_count_list.append([empty_count, idx])

    max_empty = -1e9
    for e in empty_count_list:
        max_empty = max(max_empty, e[0])

    empty_index_list = []
    for e in empty_count_list:
        if max_empty == e[0]:
            empty_index_list.append(e[1])

    # 적절한 자리가 딱 한 자리 있으면 그 자리에 배치
    if len(empty_index_list) == 1:
        room[empty_index_list[0][0]][empty_index_list[0][1]] = student
        continue

    # 3. 2를 만족하는 칸도 여러 개인 경우 행, 열의 번호가 가장 작은 칸 --> sort
    empty_index_list.sort()
    room[empty_index_list[0][0]][empty_index_list[0][1]] = student

# 만족도 구하기
result = 0
for i in range(n):
    for j in range(n):
        satisfaction = 0
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if room[nx][ny] in data[room[i][j]]:
                satisfaction += 1
        if satisfaction >= 2:
            satisfaction = 10**(satisfaction-1)
        result += satisfaction

print(result)
