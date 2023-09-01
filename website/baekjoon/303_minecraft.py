n, m, b = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer_t, answer_h = 1e9, 0
for h in range(257):
    use, get = 0, 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] > h:
                get += arr[r][c] - h
            else:
                use += h - arr[r][c]

    if use - get > b:
        continue

    t = use+get*2
    if t <= answer_t:
        answer_t, answer_h = t, h

print(answer_t, answer_h)
