array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# return
result = sorted(array)
print(result)

# 내부에서 바로 정렬
array.sort()
print(array)

# key를 활용
array = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    # 숫자를 key로
    return data[1]


result = sorted(array, key=setting)
print(result)
