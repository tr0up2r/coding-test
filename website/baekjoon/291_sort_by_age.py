n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append((i, int(age), name))

arr.sort(key=lambda x: (x[1], x[0]))
for p in arr:
    print(p[1], p[2])
