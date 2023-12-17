s = input()
answer = 10
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        answer += 5
    else:
        answer += 10
print(answer)
