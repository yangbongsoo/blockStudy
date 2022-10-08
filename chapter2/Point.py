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
		# 다른 타원곡선이기 때문에 더하기 대상이 아님.
		if self.a != other.a or self.b != other.b:
			raise TypeError('Points {}, {} are not on the same curve'.format(self, other))

		# None 은 무한원점을 의미한다. self 가 무한원점이면, other 를 리턴. ex) A(other) + I(self) = A
		if self.x is None:
			return other

		# other.x 가 무한원점이면, self 를 리턴함. ex) A(self) + I(other) = A
		if other.x is None:
			return self

		# 연습문제 2.3
		# 한 점에 그의 역원을 더하는 경우를 코딩해라.
		# 두 점은 x 가 같고 y 는 다른 경우이며 두 점을 이은 직선은 x축에 수직이다. 반환된 결과는 무한원점이어야 한다.
		if self.x == other.x and self.y != other.y:
			return self.__class__(None, None, self.a, self.b)

		# 연습문제 2.5
		if self.x != other.x:
			s = (other.y - self.y) / (other.x - self.x)
			x = s ** 2 - self.x - other.x
			y = s * (self.x - x) - self.y
			return self.__class__(x, y, self.a, self.b)

		# 연습문제 2.7
		if self == other:
			s = (3 * self.x ** 2 + self.a) / (2 * self.y)
			x = s ** 2 - 2 * self.x
			y = s * (self.x - x) - self.y
			return self.__class__(x, y, self.a, self.b)

		# 덧셈 예외처리. 접선이 x 축에 수직인 경우 p81. P1 = P2 이면서 y 좌표가 0인 경우
		if self == other and self.y == 0 * self.x:
			return self.__class__(None, None, self.a, self.b)

	def __str__(self):
		return "Point({},{})_{}_{}".format(self.x, self.y, self.a, self.b)
