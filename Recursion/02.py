def lucky(n: int, depth: int) -> int:
	if n // 10 == 0:
		return n
	else:
		digit_sum = sum(int(digit) for digit in str(n))
		if digit_sum // 10 != 0:
			print(f'Sum #{depth} : {digit_sum}')
		return lucky(digit_sum, depth + 1)

def main():
	n = int(input('Enter Input: '))
	result = lucky(n, 1)
	print(f'Lucky Number: {result}')

if __name__ == '__main__':
	main()