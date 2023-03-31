import sys
input = sys.stdin.readline

n = int(input())
array = [0]*16
array[0] = 2

for i in range(1, n+1):
    array[i] = (array[i-1]-1) + array[i-1]

print(array[n]**2)
