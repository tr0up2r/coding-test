arr = []
for _ in range(int(input())):
    n, d, m, y = input().split()
    arr.append((n, int(y), int(m), int(d)))
arr.sort(key=lambda x: (x[1], x[2], [3]))
print(arr[-1][0], arr[0][0], sep='\n')
