s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in input():
    print(s[(s.find(x)-3)%26], end='')
