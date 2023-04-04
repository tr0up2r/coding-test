from collections import deque

# 톱니바퀴는 index 1번부터 시작
data = {}
for i in range(1, 5):
    data[i] = deque(list(map(int, list(input()))))

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
        # deque를 이용한 회전
        data[idx].rotate(direction)


for rot in rotation:
    rotate(rot[0], rot[1])

print(data[1][0] + data[2][0]*2 + data[3][0]*4 + data[4][0]*8)
