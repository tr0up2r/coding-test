from collections import Counter


name = Counter(list(input()))
name = sorted(list(name.items()), key=lambda x: x[0], )
answer = ''

odd = ''
odd_count = 0
for i in range(len(name)):
    if name[i][1] % 2:
        odd_count += 1
        odd += name[i][0]
    answer += name[i][0] * (name[i][1]//2)

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    if odd_count:
        print(answer + odd + answer[::-1])
    else:
        print(answer + answer[::-1])
