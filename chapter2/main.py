from chapter2.Point import Point

# 연습문제 2.1
# p1 = Point(2, 4, 5, 7)  # False
# p2 = Point(-1, -1, 5, 7)  # True
# p3 = Point(18, 77, 5, 7)  # True
# p4 = Point(5, 7, 5, 7)  # False
# print(p2 == p2)

# 점 덧셈 코딩하기
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 7)
inf = Point(None, None, 5, 7)
print(p1 + inf)
print(p2 + inf)
print(p1 + p2)

# 연습문제 2.4
p1 = Point(2, 5, 5, 7)
p2 = Point(-1, -1, 5, 7)
print(p1 + p2)

# 연습문제 2.6
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, -1, 5, 7)
print(p1 + p2)

a, x1, y1 = 5, -1, -1
s = (3 * x1 ** 2 + a) / (2 * y1)
x3 = s ** 2 - 2 * x1
y3 = s * (x1 - x3) - y1
print(x3, y3)


