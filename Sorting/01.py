# def	bubble_sort(data):
# 	for i in range(len(data)):
# 		for j in range(len(data) - i - 1):
# 			if data[j] > data[j + 1]:
# 				tmp = data[j]
# 				data[j] = data[j + 1]
# 				data[j + 1] = tmp

def bubble_sort_recur(data, i = 0, j = 0):
	if (i < len(data)):
		if (j < len(data) - i - 1):
			if (data[j] > data[j + 1]):
				tmp	 = data[j]
				data[j] = data[j + 1]
				data[j + 1] = tmp
			bubble_sort_recur(data, i, j + 1)
		bubble_sort_recur(data, i + 1, 0)

def	main():
	inp = input('Enter Input : ').split(' ')
	inp = [int(x) for x in inp]
	inp1 = inp.copy()
	bubble_sort_recur(inp1)
	print(inp1)


if __name__ == '__main__':
	main()