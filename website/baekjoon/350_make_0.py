def dfs(nums, idx):
    if idx == n:
        if eval(nums.replace(' ', '')) == 0:
            print(nums)
        return

    for op in ops:
        tmp_nums = nums
        nums = nums + op + arr[idx]
        dfs(nums, idx+1)
        nums = tmp_nums


ops = [' ', '+', '-']

for _ in range(int(input())):
    n = int(input())
    arr = list(map(str, range(1, n+1)))
    dfs(arr[0], 1)
    print()
