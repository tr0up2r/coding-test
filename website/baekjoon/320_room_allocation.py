n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))

now = 0
count = 0
for i in range(n):
    if arr[i][0] >= now:
        count += 1
        now = arr[i][1]

print(count)
