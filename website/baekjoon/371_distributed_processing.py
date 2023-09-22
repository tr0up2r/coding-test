for _ in range(int(input())):
    a, b = map(int, input().split())
    answer = 1
    for _ in range(b):
        answer = (answer*a)%10
    print(answer if answer else 10)
