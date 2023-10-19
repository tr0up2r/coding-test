s, st = input(), set()
for i in range(1, len(s)+1):
    for j in range(len(s)+1-i):
        st.add(s[j:j+i])
print(len(st))
