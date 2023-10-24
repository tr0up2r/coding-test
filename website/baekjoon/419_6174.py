for _ in range(int(input())):
    answer = 0
    n = list(input())
    while ''.join(n) != '6174':
        n = sorted(n)
        now = int(''.join(n)[::-1])-int(''.join(n))
        n = list(str(now).zfill(4))
        answer += 1
    print(answer)
