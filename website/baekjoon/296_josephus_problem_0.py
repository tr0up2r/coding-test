from collections import deque


n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
answer = []
while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    answer.append(str(arr.popleft()))

print('<' + ', '.join(answer) + '>')
