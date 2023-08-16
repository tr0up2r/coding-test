s = list(input())
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
answer = ''

for w in s:
    if w.isalpha():
        if w.isupper():
            answer += upper[(ord(w)-ord('A')+13) % (ord('Z')-ord('A')+1)]
        else:
            answer += lower[(ord(w)-ord('a')+13) % (ord('z')-ord('a')+1)]
    else:
        answer += w

print(answer)
