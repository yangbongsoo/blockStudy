from FieldElement import FieldElement

a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a == b)
print(a == a)

a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a != b)

a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a + b == c)

# 연습문제 1.2
a = FieldElement(44, 57)
b = FieldElement(33, 57)
c = FieldElement(20, 57)
print(a + b == c)

a = FieldElement(9, 57)
b = FieldElement(29, 57)
c = FieldElement(37, 57)
print(a - b == c)

a = FieldElement(52, 57)
b = FieldElement(30, 57)
c = FieldElement(38, 57)
d = FieldElement(41, 57)
print(a - b - c == d)

# 연습문제 1.4
print((95 * 45 * 31) % 97)
print((17 * 13 * 19 * 44) % 97)
print((127 * ((77 ** 49) % 97)) % 97)
print(((12 ** 7) * (77 ** 49)) % 97)

# 연습문제 1.5
prime = 19
kSet = [1, 3, 7, 13, 18]
tempList = []
for k in kSet:
	for i in range(0, prime):
		tempList.append((k * i) % prime)
	print(sorted(tempList))
	tempList = []

# 답
for k in (1, 3, 7, 13, 18):
	print(sorted([k * i % prime for i in range(prime)]))

# 곱하기 구현
a = FieldElement(3, 13)
b = FieldElement(12, 13)
c = FieldElement(10, 13)
print(a * b == c)

# 거듭제곱 구현
a = FieldElement(3, 13)
b = FieldElement(1, 13)
print(a ** 3 == b)

# 연습문제 1.7
primes = [7, 11, 17, 31]

for p in primes:
	# print([(i ** (p - 1)) % p for i in range(1, p)])
	print([pow(i, (p - 1), p) for i in range(1, p)])  # pow 사용

# 유한체 나눗셈. 연습문제 1.9
a = FieldElement(2, 19)
b = FieldElement(7, 19)
c = FieldElement(3, 19)
print(a / b == c)

# 1.8 거듭제곱 메서드 수정
a = FieldElement(7, 13)
b = FieldElement(8, 13)
print(a ** -3 == b)
