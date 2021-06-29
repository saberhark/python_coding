def solution(phone_book):
    dic = {}
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) >= len(phone_book[i+1]):
            continue

        dic[phone_book[i]] = 1
        if phone_book[i + 1][0:len(phone_book[i])] in dic:
            return False

    return True


ans = solution(["119", "97674223", "1195524421"])

print(ans)