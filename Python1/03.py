def main():
	n = int(input("Enter number of row : "))

	for i in range(1, n+1):
		# first element is always 1
		C = 1
		for j in range(1, i+1):
			if j == 1:
				# first value in a line is always 1
				print(C, sep='', end='')
			else:
				print(' ', C, sep='', end='')


			# using Binomial Coefficient
			C = C * (i - j) // j
		print()

if __name__ == '__main__':
	main()