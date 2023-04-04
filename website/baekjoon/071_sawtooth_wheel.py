# 톱니바퀴는 index 1번부터 시작
data = [[]]
for _ in range(4):
    data.append(list(map(int, (list(input())))))  # n극은 0, s극은 1
data.append([])

rotation = []
k = int(input())
for _ in range(k):
    rotation.append(list(map(int, input().split())))  # 1: 시계 방향, -1: 반시계 방향

visited = [False] * 5


def rotate(idx, direction):
    if idx < 1 or idx > 4:
        return
    else:
        if idx - 1 >= 1 and not visited[idx - 1] and data[idx - 1][2] != data[idx][6]:
            visited[idx] = True
            rotate(idx - 1, -direction)
            visited[idx] = False
        if idx + 1 <= 4 and not visited[idx + 1] and data[idx][2] != data[idx + 1][6]:
            visited[idx] = True
            rotate(idx + 1, -direction)
            visited[idx] = False
        temp = [[] for _ in range(5)]
        for i in range(len(data)):
            for j in range(len(data[i])):
                temp[i].append(data[i][j])
        if direction == 1:
            for i in range(8):
                data[idx][i] = temp[idx][(i-1)%8]
        else:
            for i in range(8):
                data[idx][i] = temp[idx][(i+1)%8]
        temp.clear()


for rot in rotation:
    rotate(rot[0], rot[1])

print(data[1][0] + data[2][0]*2 + data[3][0]*4 + data[4][0]*8)
