from collections import Counter


for _ in range(int(input())):
    a, b = input().split()
    s = '' if Counter(a) == Counter(b) else 'NOT '
    print(f"{a} & {b} are {s}anagrams.")
