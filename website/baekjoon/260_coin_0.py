n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

count = 0
while k:
    for i in range(n):
        q = k // arr[i]
        if q > 0:
            k -= q * arr[i]
            count += q
            break

print(count)
