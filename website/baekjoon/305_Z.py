n, r, c = map(int, input().split())
answer = 0
while n:
    n -= 1
    count = (2**n) * (2**n)
    if r < 2**n and c < 2**n:
        answer += count * 0
    elif r < 2**n and c >= 2**n:
        answer += count * 1
        c -= 2**n
    elif r >= 2**n and c < 2**n:
        answer += count * 2
        r -= 2**n
    else:
        answer += count * 3
        r -= 2**n
        c -= 2**n

print(answer)
