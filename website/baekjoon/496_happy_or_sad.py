s = input()
hc, sc = s.count(':-)'), s.count(':-(')
if hc == 0 and sc == 0:
    print('none')
elif hc == sc:
    print('unsure')
elif hc > sc:
    print('happy')
else:
    print('sad')
