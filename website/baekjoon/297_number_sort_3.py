import sys


n = int(sys.stdin.readline().rstrip())
arr = [0] * 10001
for _ in range(n):
    arr[int(sys.stdin.readline().rstrip())] += 1

for i in range(1, 10001):
    for _ in range(arr[i]):
        print(i)
