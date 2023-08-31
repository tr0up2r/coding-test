n, k = map(int, input().split())
nf, kf, nkf = 1, 1, 1
for i in range(1, n+1):
    nf *= i

for i in range(1, k+1):
    kf *= i

for i in range(1, n-k+1):
    nkf *= i

print(nf // (kf * nkf))
