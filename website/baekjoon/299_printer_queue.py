from collections import deque


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque([(i, x) for i, x in enumerate(list(map(int, input().split())))])
    count = 0

    while queue:
        flag = True
        now = queue.popleft()
        for num in queue:
            if num[1] > now[1]:
                queue.append(now)
                flag = False
                break
        if flag:
            count += 1
            if now[0] == m:
                print(count)
