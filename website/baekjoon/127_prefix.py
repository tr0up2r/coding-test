n = int(input())
data = [input() for _ in range(n)]

data.sort()
answer = 0
for i in range(n):
    flag = True
    for j in range(i+1, n):
        if data[i] == data[j][0:len(data[i])]:
            flag = False
            break
    if flag:
        answer += 1

print(answer)
