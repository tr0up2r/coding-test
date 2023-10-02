from collections import deque


n = int(input())
arr = list(map(int, input().split()))
check = [-1] * n
check[0] = 0

queue = deque([(0, 0)])
while queue:
    x, t = queue.popleft()
    for i in range(1, arr[x]+1):
        nx = x+i
        if 0 <= nx < n and check[nx] == -1:
            check[nx] = t+1
            queue.append((nx, t+1))

print(check[n-1])
