def ascending_sort(data):
	sort = data.copy()
	for i in range(len(sort)):
		for j in range(len(sort) - i - 1):
			if sort[j] > sort[j + 1]:
				tmp = sort[j]
				sort[j] = sort[j + 1]
				sort[j + 1] = tmp
	return sort

def sol(data):
	current_lst = []
	current_len = 0
	for i in data:
		current_lst.append(i)
		current_len += 1
		# Even
		sort = ascending_sort(current_lst)
		pos = int(current_len / 2)
		if current_len % 2 == 0:
			left_med = sort[pos - 1]
			right_med = sort[pos]
			med = (left_med + right_med) / 2
		else:
			med = sort[pos]
		print(f'list = {current_lst} : median = {med:.1f}')


def main():
	inp = input('Enter Input : ').split(' ')
	inp = [int(x) for x in inp]
	sol(inp)

if __name__ == '__main__':
	main()