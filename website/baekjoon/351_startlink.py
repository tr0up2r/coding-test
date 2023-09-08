from collections import deque


f, s, g, u, d = map(int, input().split())
arr = [1e9]*(f+1)
arr[s] = 0

queue = deque([s])
while queue:
    now = queue.popleft()
    for b in (u, -d):
        nnow = now+b
        if 1 <= nnow <= f and arr[nnow] == 1e9:
            arr[nnow] = arr[now]+1
            queue.append(nnow)

print(arr[g] if arr[g] != 1e9 else "use the stairs")
