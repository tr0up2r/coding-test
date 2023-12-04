n, d = input().split()
answer, n = 0, int(n)
for i in range(1, n+1):
    answer += str(i).count(d)
print(answer)
