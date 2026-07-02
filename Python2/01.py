def main():
	i = input("Enter number and shiftcount : ")
	number, shift = i.split(' ')
	number = int(number)
	shift = int(shift)
	print(number >> shift)

if __name__ == '__main__':
	main()