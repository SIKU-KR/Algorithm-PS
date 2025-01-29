from itertools import combinations

def solution(phone_book):
    phone_book.sort()  # O(N log N)
    for i in range(len(phone_book) - 1):  # O(N)
        if phone_book[i+1].startswith(phone_book[i]):  # O(M)
            return False
    return True