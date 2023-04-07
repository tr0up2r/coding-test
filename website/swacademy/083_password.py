t = int(input())
answer = []

for i in range(1, t+1):
    n, k = map(int, input().split())
    data = list(input())
    s = set()
    for _ in range(n):
        last = [data[-1]]
        remain = data[:-1]
        data.clear()
        data = last + remain
        for j in range(0, n, n//4):
            s.add(tuple(data[j:j+n//4]))
    result = list(s)
    result.sort(reverse=True)
    num = int(''.join(result[k-1]), 16)
    print(f'#{i} {num}')
