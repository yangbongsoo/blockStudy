class FieldElement:

	def __init__(self, num, prime):
		if num >= prime or num < 0:
			error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
			raise ValueError(error)
		self.num = num
		self.prime = prime

	def __repr__(self):
		return 'FieldElement_{}({})'.format(self.prime, self.num)

	def __eq__(self, other):
		if other is None:
			return False
		return self.num == other.num and self.prime == other.prime

	# 연습문제 1.1
	def __ne__(self, other):
		if other is None:
			return False
		return self.num != other.num or self.prime != other.prime

	# 책 답
	# def __ne__(self, other):
	# 	return not(self == other)

	def __add__(self, other):
		if self.prime != other.prime:
			raise TypeError('Cannot add two numbers in different Fields')
		num = (self.num + other.num) % self.prime

		# FieldElement 를 사용해도 되지만, 클래스 상속 시 __add__ 메서드가 실행될 때 해당 하위 클래스가 아닌
		# FieldElement 의 인스턴스를 반환하게 고정됌
		# return FieldElement(num, self.prime)

		return self.__class__(num, self.prime)

	def __sub__(self, other):
		if self.prime != other.prime:
			raise TypeError('Cannot sub two numbers in different Fields')
		num = (self.num - other.num) % self.prime
		return self.__class__(num, self.prime)

	# 연습문제 1.6
	def __mul__(self, other):
		if self.prime != other.prime:
			raise TypeError('Cannot mul two numbers in different Fields')
		num = (self.num * other.num) % self.prime
		return self.__class__(num, self.prime)

	# 거듭제곱
	def __pow__(self, exponent):
		# num = (self.num ** exponent) % self.prime

		# pow 함수 사용
		# num = pow(self.num, exponent) % self.prime
		n = exponent % (self.prime - 1)
		num = pow(self.num, n, self.prime)  # 매 곱셈 단계에서 나머지연산으로 값의 크기를 줄이기 때문에 더 효율적
		return self.__class__(num, self.prime)

	def __truediv__(self, other):
		if self.prime != other.prime:
			raise TypeError('Cannot div two numbers in different Fields')
		num = self.num * pow(other.num, self.prime - 2) % self.prime
		return self.__class__(num, self.prime)
