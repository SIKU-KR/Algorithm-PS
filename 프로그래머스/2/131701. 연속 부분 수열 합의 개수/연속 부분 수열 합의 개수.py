def solution(elements):
    s = set()
    a = elements * 2
    for i in range(0, len(elements)):
        for j in range(0, len(elements)):
            s.add(sum(a[j:j+i]))
    return len(s)