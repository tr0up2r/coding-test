def solution(n):
    arr = [[0] * n for _ in range(n)]
    r, c = -1, 0
    num = 1

    for i in range(n):
        for _ in range(n - i):
            if i % 3 == 0:
                r += 1
            elif i % 3 == 1:
                c += 1
            elif i % 3 == 2:
                r -= 1
                c -= 1

            arr[r][c] = num
            num += 1

    answer = []
    for i in range(n):
        for j in range(i + 1):
            answer.append(arr[i][j])

    return answer
