n = int(input())
if n == 0:
    print(0)
else:
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()

    out = round((n + 0.0000001) * 0.15)
    print(round((sum(arr[out:len(arr)-out])/(n-out*2))+0.0000001))
