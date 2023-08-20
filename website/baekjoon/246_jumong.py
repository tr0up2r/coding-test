n = int(input())
m = int(input())

data = list(map(int, input().split()))
data.sort()

l, r = 0, len(data)-1
answer = 0
while l < r:
    if data[l] + data[r] == m:
        answer += 1
        l += 1
        r -= 1
    elif data[l] + data[r] < m:
        l += 1
    else:
        r -= 1

print(answer)
