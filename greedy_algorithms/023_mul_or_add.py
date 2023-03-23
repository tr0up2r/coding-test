data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if result <= 1 or num <= 1:  # 두 수 중 하나라도 1 이하의 수라면 더하기 수행
        result += num
    else:
        result *= num

print(result)
