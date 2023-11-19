def dfs(now, idx):
    if len(now) == 6:
        print(' '.join(now))
        return

    for i in range(idx, k):
        now.append(arr[i])
        dfs(now, i+1)
        now.pop()


while True:
    arr = list(input().split())
    if arr[0] == '0':
        break
    else:
        k = int(arr.pop(0))

    dfs([], 0)
    print()
