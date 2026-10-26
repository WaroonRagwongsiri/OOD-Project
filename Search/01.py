def fake_sqrt(n):
	if n < 0:
		return None

	i = 0
	while i * i <= n:
		if i * i == n:
			return i
		i = i + 1
	return i - 1

def main():
	inp = input('Enter Input : ')
	root = fake_sqrt(int(inp))
	if root == None:
		print('Invalid input')
	else:
		print(root)

if __name__ == '__main__':
	main()