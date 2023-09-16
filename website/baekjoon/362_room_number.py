n = input()
arr = [0]*10
for x in n:
    x = int(x)
    if x == 6 or x == 9:
        if arr[9] > arr[6]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[x] += 1
print(max(arr))
