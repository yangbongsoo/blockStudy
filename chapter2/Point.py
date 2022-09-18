class Point:

	def __init__(self, x, y, a, b):
		self.a = a
		self.b = b
		self.x = x
		self.y = y
		if self.y ** 2 != self.x ** 3 + a * x + b:  # 주어진 점이 곡선 위에 있는지 검사
			raise ValueError('({}, {}) is not on the curve'.format(x, y))

	def __eq__(self, other):  # 두 점은 같은 곡선 위에 있고 그 좌푯값이 동일해야 함
		return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

	# 연습문제 2.2
	def __ne__(self, other):
		return not (self == other)
