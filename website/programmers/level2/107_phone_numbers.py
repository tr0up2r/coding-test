def solution(phone_book):
    set_phone_book = set(phone_book)
    for i in range(len(phone_book)):
        temp = ''
        for s in phone_book[i]:
            temp += s
            if temp != phone_book[i] and temp in set_phone_book:
                return False
    return True
