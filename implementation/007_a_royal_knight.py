# 8*8 평면상에서 나이트가 위치한 곳의 좌표를 나타내는 두 문자가 입력됨.

location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a'))+1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
count = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8:
        count += 1

print(count)