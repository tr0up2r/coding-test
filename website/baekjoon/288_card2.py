from collections import deque


n = int(input())
arr = deque([x for x in range(1, n+1)])
while True:
    if len(arr) <= 1:
        break
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])
