from collections import Counter


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

print(round(sum(arr)/n))
print(arr[n//2])
c = Counter(arr).most_common()
if len(c) > 2 and c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])
print(arr[-1] - arr[0])
