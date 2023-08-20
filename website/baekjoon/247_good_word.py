n = int(input())
answer = 0

for _ in range(n):
    s = input()
    stack = []

    for w in s:
        if stack and w == stack[-1]:
            stack.pop()
        else:
            stack.append(w)

    if not stack:
        answer += 1

print(answer)
