n = int(input())
arr = set()

for _ in range(n):
    arr.add(input())
arr = sorted(arr, key=(lambda x: (len(x), x)))

for w in arr:
    print(w)
