for _ in range(int(input())):
    print(*list(map(lambda x: x[::-1], input().split())))
