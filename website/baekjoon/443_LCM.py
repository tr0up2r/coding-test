for _ in range(int(input())):
    A, B = map(int, input().split())
    a, b = A, B
    while a != b:
        if a < b:
            a += A
        else:
            b += B
    print(a)
