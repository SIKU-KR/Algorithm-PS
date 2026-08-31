def solution(sizes):
    width = max(max(w, h) for w, h in sizes)
    height = max(min(w, h) for w, h in sizes)
    return width * height