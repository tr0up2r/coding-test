from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
queue = deque()
queue.append([n, 0])
min_count = 1e9
path = 0

while queue:
    x, count = queue.popleft()
    visited[x] = True
    if x == k:
        if path == 0:
            min_count = count
            path += 1
        else:
            if min_count == count:
                path += 1
    for nx in (2 * x, x - 1, x + 1):
        if 0 <= nx <= 100000 and not visited[nx]:
            queue.append([nx, count + 1])

print(min_count)
print(path)
