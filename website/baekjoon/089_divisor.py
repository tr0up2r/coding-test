n, k = map(int, input().split())
find = False
count = 0

for i in range(1, n//2+2):
    if not n%i:
        count += 1
    if count == k:
        print(i)
        find = True
        break

if count+1 == k:
    print(n)
elif not find:
    print(0)
