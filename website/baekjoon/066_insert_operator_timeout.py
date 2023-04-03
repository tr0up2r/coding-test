import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
data = list(input().split())
temp = []

# 덧, 뺄, 곱, 나의 개수
ops_num = list(map(int, input().split()))
ops = ['+', '-', '*', '//']
real_ops = []
for op, num in zip(ops, ops_num):
    for _ in range(num):
        real_ops.append(op)

max_result = -1e9
min_result = 1e9

ops_permutations = list(permutations(real_ops, n-1))

for ops_per in ops_permutations:
    temp = data.copy()
    for i in range(0, n-1):
        if (ops_per[i] == '//') and (int(temp[i]) < 0) and (int(temp[i+1]) >= 0):
            temp[i+1] = -(-(int(temp[i])) // int(temp[i+1]))
        else:
            temp[i+1] = eval(f'{temp[i]}{ops_per[i]}{temp[i+1]}')
    result = temp[n-1]
    max_result = max(result, max_result)
    min_result = min(result, min_result)

print(max_result)
print(min_result)