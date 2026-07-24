def staircase_pos(n: int, i: int, lines: list):
	if i < 0:
		return
	lines.append("_" * i + "#" * (n - i))
	staircase_pos(n, i - 1, lines)

def staircase_neg(m: int, i: int, lines: list):
	if i == m:
		return
	lines.append("_" * i + "#" * (m - i))
	staircase_neg(m, i + 1, lines)

def staircase(n: int):
	if n == 0:
		return "Not Draw!"

	lines = []
	if n > 0:
		staircase_pos(n, n - 1, lines)
	else:
		staircase_neg(abs(n), 0, lines)

	return "\n".join(lines)

def main():
	print(staircase(int(input("Enter Input : "))))

if __name__ == '__main__':
	main()