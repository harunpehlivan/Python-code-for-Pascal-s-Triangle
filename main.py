# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
for i in range(n):
	for _ in range(n-i+1):
		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	print()

# Print Pascal's Triangle in Python

# input n
n = 5

for i in range(1, n+1):
	for _ in range(n-i+1):
		print(' ', end='')

	# first element is always 1
	C = 1
	for j in range(1, i+1):

		# first value in a line is always 1
		print(' ', C, sep='', end='')

		# using Binomial Coefficient
		C = C * (i - j) // j
	print()

# Print Pascal's Triangle in Python

# input n
n = 5

# iterarte upto n
for i in range(n):
	# adjust space
	print(' '*(n-i), end='')

	# compute power of 11
	print(' '.join(map(str, str(11**i))))

