# 첫번째 위치를 찾는 이진 탐색
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    if target == array[mid] and (mid == 0 or target > array[mid-1]):
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)


def last(array, target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    if target == array[mid] and (mid == n-1 or target < array[mid+1]):
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)


def count_by_value(array, target):
    n = len(array)
    a = first(array, target, 0, n-1)

    if a is None:
        return 0

    b = last(array, target, 0, n-1)

    return b-a+1


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)
