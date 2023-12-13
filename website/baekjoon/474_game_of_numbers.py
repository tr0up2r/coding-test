m, n = map(int, input().split())
d = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
     '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
arr = []
for x in range(m, n+1):
    now = ''
    for s in str(x):
        now += d[s]
    arr.append((x, now))
arr.sort(key=lambda x: x[1])
result = [arr[i:i+10] for i in range(0, len(arr), 10)]
for line in result:
    print(' '.join(map(str, map(lambda x: x[0], line))))
