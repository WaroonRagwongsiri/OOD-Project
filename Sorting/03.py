def ascending_sort(data):
	sort = data.copy()
	for i in range(len(sort)):
		for j in range(len(sort) - i - 1):
			if sort[j] > sort[j + 1]:
				tmp = sort[j]
				sort[j] = sort[j + 1]
				sort[j + 1] = tmp
	return sort

def descending_sort(data):
	sort = data.copy()
	for i in range(len(sort)):
		for j in range(len(sort) - i - 1):
			if sort[j] < sort[j + 1]:
				tmp = sort[j]
				sort[j] = sort[j + 1]
				sort[j + 1] = tmp
	return sort

def sol(data):
	asc = ascending_sort(data)
	des = descending_sort(data)
	unique = len(set(data))

	if (unique == 1):
		return "Repdrome"
	elif asc == data and len(data) == unique:
		return "Metadrome"
	elif asc == data and len(data) != unique:
		return "Plaindrome"
	elif des == data and len(data) == unique:
		return "Katadrome"
	elif des == data and len(data) != unique:
		return "Nialpdrome"
	return "Nondrome"


def main():
	inp = input('Enter Input : ')
	inp = [int(x) for x in inp]
	print(sol(inp))

if __name__ == '__main__':
	main()