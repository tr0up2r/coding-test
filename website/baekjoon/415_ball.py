arr = list(range(4))
for _ in range(int(input())):
    x, y = map(int, input().split())
    i, j = arr.index(x), arr.index(y)
    arr[i], arr[j] = arr[j], arr[i]
print(arr[1])
