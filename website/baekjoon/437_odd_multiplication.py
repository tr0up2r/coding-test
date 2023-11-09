A, B = input().split()
answer = 0
for a in A:
    for b in B:
        answer += int(a)*int(b)
print(answer)
