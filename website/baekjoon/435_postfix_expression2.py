n = int(input())
ops = input()
stack, nums = [], [0]*26
for i in range(n):
    nums[i] = int(input())

for op in ops:
    if op in ['+', '-', '*', '/']:
        a, b = stack.pop(), stack.pop()
        stack.append(eval(f'{b}{op}{a}'))
    else:
        stack.append(nums[ord(op)-65])
print(f'{stack[0]:.2f}')
