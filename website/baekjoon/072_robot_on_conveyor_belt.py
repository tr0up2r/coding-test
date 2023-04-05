n, k = map(int, input().split())
data = list(map(int, input().split()))

result = 0
robot_idx = []
while True:
    result += 1

    # 1. 회전
    last = [data[-1]]
    remain = data[:n*2-1]
    data.clear()
    data = last + remain
    for i in range(len(robot_idx)):
        robot_idx[i] += 1
    if n-1 in robot_idx:
        robot_idx.remove(n-1)

    for i in range(len(robot_idx)):
        if data[robot_idx[i]+1] < 1:
            continue
        if robot_idx[i]+1 in robot_idx:
            continue
        robot_idx[i] += 1
        data[robot_idx[i]] -= 1

    if n-1 in robot_idx:
        robot_idx.remove(n-1)

    # 3. 로봇 올리기
    if data[0] > 0 and (0 not in robot_idx):
        robot_idx.append(0)
        data[0] -= 1

    count = 0
    for i in range(len(data)):
        if data[i] == 0:
            count += 1

    if count >= k:
        break

print(result)
