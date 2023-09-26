import sys


n, m = map(int, input().split())
s = set()
answer = 0
for _ in range(n):
    s.add(sys.stdin.readline().rstrip())
for _ in range(m):
    if sys.stdin.readline().rstrip() in s:
        answer += 1
print(answer)
