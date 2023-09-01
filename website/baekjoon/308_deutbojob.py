import sys


input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
s = set()
answer = []

for _ in range(n):
    s.add(input().rstrip())
for _ in range(m):
    now = input().rstrip()
    if now in s:
        answer.append(now)

answer.sort()
print(len(answer))
for name in answer:
    print(name)
