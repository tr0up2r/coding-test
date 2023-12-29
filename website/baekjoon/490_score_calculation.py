arr = [(i, int(input())) for i in range(1, 9)]
arr.sort(key=lambda x: -x[1])
print(sum(x[1] for x in arr[:5]))
print(*sorted([x[0] for x in arr[:5]]))
