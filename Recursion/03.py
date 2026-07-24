def permu_paren(p: int, current_str: str = "", open_count: int = 0, close_count: int = 0, results: list = None) -> list:
	if results is None:
		results = []

	if len(current_str) == 2 * p:
		results.append(current_str)
		return results

	if open_count < p:
		permu_paren(p, current_str + '(', open_count + 1, close_count, results)

	if close_count < open_count:
		permu_paren(p, current_str + ')', open_count, close_count + 1, results)

	return results

def main():
	p = int(input('Enter number of pair parenthesis(es): '))

	valid_parentheses = permu_paren(p)

	print('All possible parenthesis(es)')
	print(",".join(valid_parentheses))

if __name__ == '__main__':
	main()