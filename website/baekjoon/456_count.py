from collections import Counter


int(input())
c = Counter(list(map(int, input().split())))
print(c[int(input())])
