arr = []
for _ in range(int(input())):
    arr.append(input())
print(max(sorted(arr), key=arr.count))
