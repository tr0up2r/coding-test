n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
answer = [0, 0]


def cut_paper(sr, sc, size):
    now = arr[sr][sc]
    if size == 1:
        answer[now] += 1
        return

    for r in range(sr, sr+size):
        for c in range(sc, sc+size):
            if arr[r][c] != now:
                size //= 2
                cut_paper(sr, sc, size)
                cut_paper(sr, sc+size, size)
                cut_paper(sr+size, sc, size)
                cut_paper(sr+size, sc+size, size)
                return

    answer[now] += 1
    return


cut_paper(0, 0, n)
for x in answer:
    print(x)
