# 리스트가 정렬되어 있는 경우 O(N) (전부 if에 걸리지 않기 때문)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array = [1, 2, 3, 4, 6, 5]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
