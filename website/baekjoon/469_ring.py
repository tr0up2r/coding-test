p = input()
answer = 0
for _ in range(int(input())):
    if (input()*2).find(p) != -1:
        answer += 1
print(answer)
