answer = 0
arr = [list(input()) for _ in range(8)]
for r in range(8):
    if r%2:
        s = 1
    else:
        s = 0
    for c in range(s, 8, 2):
        if arr[r][c] == 'F':
            answer += 1
print(answer)
