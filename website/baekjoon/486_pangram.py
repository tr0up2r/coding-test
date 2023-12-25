while True:
    x = input().replace(' ', '')
    if x == '*':
        break
    print('N' if len(set(list(x))) < 26 else 'Y')
