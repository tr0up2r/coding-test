exp = input().split('-')
answer = 0

for num in exp[0].split('+'):
    answer += int(num)
for seq in exp[1:]:
    for num in seq.split('+'):
        answer -= int(num)

print(answer)
