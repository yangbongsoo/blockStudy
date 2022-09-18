from chapter2.Point import Point

# 연습문제 2.1
p1 = Point(2, 4, 5, 7)  # False
p2 = Point(-1, -1, 5, 7)  # True
p3 = Point(18, 77, 5, 7)  # True
p4 = Point(5, 7, 5, 7)  # False

print(p2 == p2)
