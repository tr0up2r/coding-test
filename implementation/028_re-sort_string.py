s = input()
result = []
summary = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        summary += int(i)

result.sort()

if summary != 0:
    result.append(str(summary))

print(''.join(result))
