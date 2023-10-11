arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))


def check(arr):
    bingo = 0

    for r in range(5):
        if sum(arr[r]) == 0:
            bingo += 1

    for c in range(5):
        s = 0
        for r in range(5):
            s += arr[r][c]
        if s == 0:
            bingo += 1

    up, down = 0, 0
    for i in range(5):
        up += arr[i][4-i]
        down += arr[i][i]
    if not up:
        bingo += 1
    if not down:
        bingo += 1

    return bingo


def main():
    answer = 0
    for _ in range(5):
        nums = list(map(int, input().split()))
        for n in nums:
            for r in range(5):
                for c in range(5):
                    if arr[r][c] == n:
                        arr[r][c] = 0
                        answer += 1
                    if answer >= 12:
                        if check(arr) >= 3:
                            return answer


print(main())
