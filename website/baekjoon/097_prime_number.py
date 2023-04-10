n = int(input())


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


data = list(map(int, input().split()))
count = 0
for num in data:
    if is_prime(num):
        count += 1
print(count)
