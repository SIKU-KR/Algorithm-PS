n, m, l, k = map(int, input().split())

stars = []
for i in range(k):
	x, y = map(int, input().split())
	stars.append((x, y))

max_count = 0
for i in range(k):
	for j in range(k):
		# 트램펄린의 왼쪽 상단 모서리를 (stars[i].x, stars[j].y)로 설정
		x1 = stars[i][0]
		y1 = stars[j][1]
		x2 = x1 + l
		y2 = y1 + l
		
		count = 0
		for star in stars:
			# 별똥별이 트램펄린 영역 안에 있는지 확인
			if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:
				count += 1
		max_count = max(max_count, count)

print(k - max_count)    