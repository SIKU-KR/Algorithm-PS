def solution(s):
    while s:
        st = []
        for ch in s:
            if st and st[-1] == ch:
                st.pop()
            else:
                st.append(ch)
        if len(s) == len(st):
            return 0
        s = "".join(st)
    return 1
            