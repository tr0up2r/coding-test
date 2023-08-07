from collections import Counter


data = Counter(list(input().lower())).most_common()
answer = data[0][0].upper()
max_count = data[0][1]

if len(data) > 1 and data[1][1] == max_count:
    print('?')
else:
    print(answer)
