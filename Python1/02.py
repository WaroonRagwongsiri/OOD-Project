def main():
	print("*** multiplication or sum ***")
	n = input("Enter num1 num2 : ")
	n1, n2 = n.split(' ')
	n1 = int(n1)
	n2 = int(n2)
	mul = n1 * n2
	add = n1 + n2
	if mul <= 1000:
		print(f'The result is {mul}')
	else:
		print(f'The result is {add}')

if __name__ == '__main__':
	main()