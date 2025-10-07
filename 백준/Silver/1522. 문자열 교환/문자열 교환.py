s = input()
a_count = s.count('a')

s += s[0:a_count-1]
min_val = 999999999
for i in range(len(s)-(a_count-1)):
	min_val = min(min_val, s[i:i+a_count].count('b'))
print(min_val)
