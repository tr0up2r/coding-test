n, L = map(int, input().split())
H = sorted(list(map(int, input().split())))
for h in H:
    if L < h:
        break
    L += 1
print(L)
