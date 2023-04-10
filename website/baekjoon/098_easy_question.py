a, b = map(int, (input().split()))

d = [0]*(b+1)
i, j = 1, 0
k = 1
while i <= b:
    if j == k:
        j = 0
        k += 1
    d[i] = k
    i += 1
    j += 1

result = 0
for i in range(a, b+1):
    result += d[i]
print(result)
