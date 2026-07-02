def main():
	print("*** Fun with Drawing ***")
	n = int(input("Enter input : "))

	width = 4 * n - 3

	for i in range(n):
		start1, end1 = (n - 1) - i, (n - 1) + i
		start2, end2 = (3 * n - 3) - i, (3 * n - 3) + i

		for j in range(width):
			if (start1 <= j <= end1) or (start2 <= j <= end2):
				if j in (start1, end1, start2, end2):
					print("*", end="")
				else:
					print("+", end="")
			else:
				print(".", end="")
		print()

	for i in range(2 * n - 2):
		start = i + 1 
		end = (width - 1) - start

		if start > end:
			break

		for j in range(width):
			if start <= j <= end:
				if j in (start, end):
					print("*", end="")
				else:
					print("+", end="")
			else:
				print(".", end="")
		print()

if __name__ == '__main__':
	main()