n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
arr.sort()

for t in target:
    start, end = 0, len(arr)-1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < t:
            start = mid+1
        elif arr[mid] > t:
            end = mid-1
        else:
            answer = 1
            break
    print(answer, end=' ')
