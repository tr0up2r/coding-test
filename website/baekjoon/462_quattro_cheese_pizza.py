int(input())
cheese = list(set(input().split()))
count = 0
for c in cheese:
    if c.endswith('Cheese'):
        count += 1
print('yummy' if count >= 4 else 'sad')
