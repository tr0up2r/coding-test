t = int(input())
tri = [(i * (i + 1) // 2) for i in range(1, 45)]


def is_triangle(n):
    for i in tri:
        for j in tri:
            for k in tri:
                if i + j + k == n:
                    return 1
    return 0


for _ in range(t):
    n = int(input())
    print(is_triangle(n))
