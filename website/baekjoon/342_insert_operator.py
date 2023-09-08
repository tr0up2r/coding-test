n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
answer = [-1e10, 1e10]


def dfs(now, idx):
    if idx == len(nums)-1:
        answer[0] = max(answer[0], now)
        answer[1] = min(answer[1], now)
        return

    for i in range(4):
        if ops[i]:
            ops[i] -= 1
            tmp = now
            if i == 0:
                tmp += nums[idx+1]
            elif i == 1:
                tmp -= nums[idx+1]
            elif i == 2:
                tmp *= nums[idx+1]
            else:
                if tmp < 0:
                    tmp *= -1
                    tmp = -(tmp // nums[idx+1])
                else:
                    tmp //= nums[idx+1]
            dfs(tmp, idx+1)
            ops[i] += 1


dfs(nums[0], 0)
for v in answer:
    print(v)
