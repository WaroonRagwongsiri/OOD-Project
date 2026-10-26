def seq_search(lst, key):
	index = 1
	for index, item in enumerate(lst):
		if item == key:
			if index != 0:
				swapped = lst[index - 1]
				tmp = lst[index]
				lst[index] = lst[index - 1]
				lst[index - 1] = tmp
				msg = f"Search {key}\n-> found at {index + 1}, swap with {swapped}\n-> {' '.join(lst)}\n"
			else:
				msg = f"Search {key}\n-> found at 1, already at front\n-> {' '.join(lst)}\n"
			return index + 1, msg
	return -1, f"Search {key}\n-> not found\n-> {' '.join(lst)}\n"


def main():
	items, search = input('Enter Input : ').split('/')
	items = items.strip().split(' ')
	search = search.strip().split(' ')

	total_cost = []
	for index, item in enumerate(search):
		cost, msg = seq_search(items, item)
		print(msg)
		if cost != -1:
			total_cost.append(cost)
			
	print(f"Final rack : {' '.join(items)}")
	print(f"Total cost : {' + '.join(map(str, total_cost))} = {sum(total_cost)}")

if __name__ == '__main__':
	main()