n = input()
length = len(n)
left = n[:length//2]
right = n[length//2:]

result = [0] * 2

for l, r in zip(left, right):
    result[0] += int(l)
    result[1] += int(r)

if result[0] == result[1]:
    print('LUCKY')
else:
    print('READY')

'''
답지 정답

n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print('READY')
'''
