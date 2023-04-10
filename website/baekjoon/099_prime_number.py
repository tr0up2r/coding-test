m = int(input())
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


primes = []
for i in range(m, n+1):
    if is_prime(i):
        primes.append(i)

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])
