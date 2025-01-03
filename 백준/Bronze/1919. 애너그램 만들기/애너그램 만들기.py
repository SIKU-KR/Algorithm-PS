from collections import Counter

a = input().strip()
b = input().strip()

counter_a = Counter(a)
counter_b = Counter(b)

a_diff = counter_a - counter_b
b_diff = counter_b - counter_a

result = sum(a_diff.values()) + sum(b_diff.values())

print(result)
