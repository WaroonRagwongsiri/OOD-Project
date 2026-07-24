def fib(n: int):
	if n <= 1:
		return (n)
	return fib(n - 1) + fib(n - 2)

def main():
	n = int(input('Enter Number : '))
	print(f'fibo({n}) = {fib(n)}')

if __name__ == '__main__':
	main()