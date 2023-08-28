n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

while len(arr) > 1:
    arr[0] += arr.pop() / 2

print(arr[0])
