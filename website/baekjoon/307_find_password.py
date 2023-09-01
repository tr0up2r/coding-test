import sys


input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
d = dict()

for _ in range(n):
    site, pw = input().rstrip().split()
    d[site] = pw

for _ in range(m):
    print(d[input().rstrip()])
