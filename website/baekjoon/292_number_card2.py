from collections import Counter


n = int(input())
c = Counter(list(map(int, input().split())))

m = int(input())
tgt = list(map(int, input().split()))
for num in tgt:
    print(c[num], end=' ')
