n, m = map(int, input().split())
arr = [[m+1]*100 for _ in range(100)]
for _ in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1-1, r2):
        for c in range(c1-1, c2):
            arr[r][c] = max(0, arr[r][c]-1)
answer = 0
for x in arr:
    answer += x.count(0)
print(answer)
