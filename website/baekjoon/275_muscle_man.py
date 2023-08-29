n = int(input())
arr = list(map(int, input().split()))
arr.sort()
max_loss = 0
if len(arr) % 2:
    max_loss = arr[-1]
    arr = arr[:len(arr)-1]

l, r = 0, len(arr)-1
while l < r:
    max_loss = max(max_loss, arr[l]+arr[r])
    l += 1
    r -= 1

print(max_loss)
