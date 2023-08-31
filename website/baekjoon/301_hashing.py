l = int(input())
s = input()
answer = 0
for i in range(l):
    answer += (ord(s[i])-ord('a')+1) * (31**i)
print(answer % 1234567891)
