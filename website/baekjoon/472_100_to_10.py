n, m = map(int, input().split(':'))
N, M = n, m
while n%m:
    n, m = m, n%m
print(f'{N//m}:{M//m}')
