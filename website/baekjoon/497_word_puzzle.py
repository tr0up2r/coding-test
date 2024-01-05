from collections import Counter


i = 1
while True:
    a, b = input(), input()
    if a == b == 'END':
        break
    answer = "same" if Counter(a) == Counter(b) else "different"
    print(f"Case {i}: {answer}")
    i += 1
