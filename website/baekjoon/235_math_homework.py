from collections import deque


n = int(input())
answer = []
temp = ''

for _ in range(n):
    line = deque(list(input()))
    while line:
        now = line.popleft()
        if now.isdigit():
            temp += now
        else:
            if temp:
                answer.append(int(temp))
                temp = ''
    if temp:
        answer.append(int(temp))
    temp = ''

answer.sort()
for num in answer:
    print(num)
