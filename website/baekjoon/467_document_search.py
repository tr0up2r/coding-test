doc, word = input(), input()
answer = 0
while True:
    i = doc.find(word)
    if i == -1:
        break
    doc = doc[i+len(word):]
    answer += 1
print(answer)

# short but slow
# print(input().count(input()))
