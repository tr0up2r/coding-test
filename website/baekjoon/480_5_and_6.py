a, b = input().split()
for n, m in zip(['6', '5'], ['5', '6']):
    print(sum(map(int, (map(lambda x: x.replace(n, m), [a, b])))), end=' ')
