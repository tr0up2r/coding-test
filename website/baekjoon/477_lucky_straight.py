arr = list(map(int, list(input())))
print('LUCKY' if sum(arr[:len(arr)//2]) == sum(arr[len(arr)//2:]) else 'READY')
