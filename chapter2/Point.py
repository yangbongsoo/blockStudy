class Point:

	def __init__(self, x, y, a, b):
		self.a = a
		self.b = b
		self.x = x
		self.y = y
		if self.x is None and self.y is None:  # 무한원점을 의미하는 None 값이 인수로 들어오면 이후의 방정식 로직 확인 안함
			return

		if self.y ** 2 != self.x ** 3 + a * x + b:  # 주어진 점이 곡선 위에 있는지 검사
			raise ValueError('({}, {}) is not on the curve'.format(x, y))

	def __eq__(self, other):  # 두 점은 같은 곡선 위에 있고 그 좌푯값이 동일해야 함
		return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

	# 연습문제 2.2
	def __ne__(self, other):
		return not (self == other)

	def __add__(self, other):
		if self.a != other.a or self.b != other.b:
			raise TypeError('Points {}, {} are not on the same curve'.format(self, other))
		if self.x is None:  # self 가 무한원점, 즉 덧셈에 대한 항등원이라는 뜻이므로 other 를 리턴.
			return other
		if other.x is None:  # 마찬가지로 other.x 가 항등원이라는 뜻이므로 self 를 리턴
			return self

		# 연습문제 2.3
		# 한 점에 그의 역원을 더하는 경우를 코딩해라.
		# 두 점은 x 가 같고 y 는 다른 경우이며 두 점을 이은 직선은 x축에 수직이다. 반환된 결과는 무한원점이어야 한다.
		if self.x == other.x and self.y != other.y:
			return self.__class__(None, None, self.a, self.b)
