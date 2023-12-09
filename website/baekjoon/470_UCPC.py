answer, i = 'UCPC', 0
for s in input().replace(' ', ''):
    if s == answer[i]:
        i += 1
    if i == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')
