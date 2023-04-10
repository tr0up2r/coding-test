n = int(input())
data = list(map(int, input().split()))


def quick_sort(data, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    quick_sort(data, start, right-1)
    quick_sort(data, right+1, end)


quick_sort(data, 0, len(data)-1)
print(data[0], data[n-1])
