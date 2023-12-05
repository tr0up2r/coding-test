for _ in range(int(input())):
    n, m = map(int, input().split())
    print(sum(map(lambda x: x.count('0'), map(str, list(range(n, m+1))))))
