from collections import deque


ops = ['D', 'S', 'L', 'R']


def bfs(a):
    queue = deque([(a, '')])
    visited = [0] * 10001
    visited[a] = 1
    while queue:
        a, now = queue.popleft()
        for op in ops:
            nnow = now
            if op == 'D':
                na = (a*2)%10000
            elif op == 'S':
                na = (a-1)%10000
            elif op == 'L':
                na = (a%1000)*10 + a//1000
            else:
                na = (a%10)*1000 + (a//10)
            nnow += op
            if na == b:
                return nnow
            if not visited[na]:
                queue.append((na, nnow))
                visited[na] = 1


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bfs(a))
