import sys


n, m = map(int, input().split())
names = dict()

for i in range(1, n+1):
    names[sys.stdin.readline().rstrip()] = i

nums = dict(map(reversed, names.items()))

for _ in range(m):
    now = sys.stdin.readline().rstrip()
    if now.isalpha():
        print(names[now])
    else:
        print(nums[int(now)])
