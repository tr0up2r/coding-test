n, m, k = map(int, input().split())
arr = [list(input()) for _ in range(n)]

answer, count = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            count += 1
        else:
            if count >= k:
                answer += count-k+1
            count = 0
    if count >= k:
        answer += count-k+1
    count = 0

print(answer)
