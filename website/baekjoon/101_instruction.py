n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(input()))

essential = {'a', 'c', 'i', 'n', 't'}
alpha = set()


def make_comb(idx, now_list):
    if len(now_list) == k:
        comb_list.append(set(now_list[:]))
    for i in range(idx, len(alpha)):
        make_comb(i+1, now_list+[alpha[i]])


new_data = []
if k < 5:
    print(0)
else:
    k -= 5  # 필수 단어 말고 배울 수 있는 단어 수
    count = 0
    for i in range(len(data)):
        word = data[i][4:len(data[i])-4]
        w_list = set()
        min_alp = set()
        for s in word:
            if s in essential:
                continue
            w_list.add(s)
            alpha.add(s)
        new_data.append(w_list)
    alpha = list(alpha)

    if len(alpha) < k:
        print(n)
    else:
        comb_list = []
        make_comb(0, [])

        max_count = -1e9
        for comb in comb_list:
            count = 0
            for word in new_data:
                if len(word - comb) == 0:
                    count += 1
            max_count = max(max_count, count)

        print(max_count)
