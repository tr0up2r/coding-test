from collections import Counter


def solution(str1, str2):
    str1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    if not str1 and not str2:
        return 1 * 65536

    c1, c2 = Counter(str1), Counter(str2)

    return int(sum((c1 & c2).values()) / sum((c1 | c2).values()) * 65536)
