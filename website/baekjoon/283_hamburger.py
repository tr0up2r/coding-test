n, k = map(int, input().split())
data = list(input())
answer = 0

for i in range(len(data)):
    if data[i] == 'P':
        for j in range(-k, k+1, 1):
            if 0 <= i+j < n and data[i+j] == 'H':
                data[i+j] = '-'
                answer += 1
                break

print(answer)
