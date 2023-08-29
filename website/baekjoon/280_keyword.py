import sys


n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input())

for _ in range(m):
    s -= set(sys.stdin.readline().rstrip().split(','))
    print(len(s))
