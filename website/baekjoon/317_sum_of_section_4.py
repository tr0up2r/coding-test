import sys


n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n):
    arr[i] += arr[i-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    i -= 1
    j -= 1
    print(arr[j] if i == 0 else arr[j]-arr[i-1])
