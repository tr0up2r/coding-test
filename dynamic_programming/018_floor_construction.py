n = int(input())

'''
n=1
2*1
1

n=2
2*1 *2 
1*2 *2
2*2
3

n=3
n=2 + n=1*2

ai = ai-1 + ai-2*2
'''

d = [0] * 101
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + (d[i-2]*2)) % 796796

print(d[n])
