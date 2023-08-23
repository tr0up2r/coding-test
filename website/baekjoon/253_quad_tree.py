n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, list(input()))))


def quad(start_r, start_c, size):
    if size == 1:
        print(data[start_r][start_c], end='')
        return

    num = data[start_r][start_c]

    for r in range(start_r, start_r+size):
        for c in range(start_c, start_c+size):
            if data[r][c] != num:
                print('(', end='')
                size //= 2
                quad(start_r, start_c, size)
                quad(start_r, start_c+size, size)
                quad(start_r+size, start_c, size)
                quad(start_r+size, start_c+size, size)
                print(')', end='')
                return

    print(num, end='')
    return


quad(0, 0, n)
