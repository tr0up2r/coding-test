num = input()
start, now = 0, 1
while start < len(num):
    for n in str(now):
        if num[start:start+1] in n:
            start += 1
    now += 1

print(now-1)
