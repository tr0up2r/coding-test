n, k = map(int, input().split())
arr = list(range(n+1))

m = 2
while m <= n and k:
    for i in range(m, n+1, m):
        if arr[i]:
            k -= 1
            arr[i] = 0
            if k == 0:
                print(i)
                break
    m += 1
