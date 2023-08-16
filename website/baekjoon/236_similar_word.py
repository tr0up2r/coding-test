from collections import Counter


n = int(input())
c_target = Counter(list(input()))
answer = 0

for i in range(n-1):
    c_now = Counter(list(input()))
    if max(sum(list((c_target - c_now).values())), sum(list((c_now - c_target).values()))) <= 1:
        answer += 1

print(answer)
