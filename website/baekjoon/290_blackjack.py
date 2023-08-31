n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            now = arr[i] + arr[j] + arr[k]
            if now <= m:
                answer = max(answer, now)

print(answer)
