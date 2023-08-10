from collections import deque


vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    pw = input()
    if pw == 'end':
        break

    flag = False
    for w in pw:
        if w in vowels:
            flag = True
            break

    pw_list = deque(list(pw))

    stack = []
    while pw_list and flag:
        now = pw_list.popleft()
        if not stack:
            stack.append(now)
        else:
            if (now in vowels and stack[-1] not in vowels) or (now not in vowels and stack[-1] in vowels):
                stack.clear()
            elif now == stack[-1]:
                if now == 'e' or now == 'o':
                    continue
                else:
                    flag = False
                    break
            stack.append(now)

            if len(stack) == 3:
                flag = False
                break

    result = "acceptable." if flag else "not acceptable."

    print(f"<{pw}> is " + result)
