def ascending_sort(data):
	sort = data.copy()
	for i in range(len(sort)):
		for j in range(len(sort) - i - 1):
			if sort[j] > sort[j + 1]:
				tmp = sort[j]
				sort[j] = sort[j + 1]
				sort[j + 1] = tmp
	return sort

def get_combinations(arr, size):
	# Basecase
	if size == 0:
		return [[]]
	if not arr:
		return []

	# INCLUDE the first number
	with_first = [[arr[0]] + rest for rest in get_combinations(arr[1:], size - 1)]

	# EXCLUDE the first number
	without_first = get_combinations(arr[1:], size)

	return with_first + without_first

def sol(target, data, current_size=1):
	all_sol = []

	# Basecase
	if current_size > len(data):
		return []

	combs = get_combinations(data, current_size)
	for c in combs:
		if sum(c) == target:
			all_sol.append(c)

	all_sol.extend(sol(target, data, current_size + 1))
	return all_sol

def compare_lst(lst1, lst2):
	# Compare len first
	if len(lst1) > len(lst2):
		return 1
	if len(lst1) < len(lst2):
		return -1

	# If lengths are equal, compare elementwise
	for i in range(len(lst1)):
		if lst1[i] > lst2[i]:
			return 1
		if lst1[i] < lst2[i]:
			return -1

	# If exactly the same
	return 0

def sort_sol(data):
	sort = data.copy()
	for i in range(len(sort)):
		for j in range(len(sort) - i - 1):
			if compare_lst(sort[j], sort[j + 1]) == 1:
				tmp = sort[j]
				sort[j] = sort[j + 1]
				sort[j + 1] = tmp
	return sort

def main():
	inp = input('Enter Input : ').split('/')
	target = int(inp[0])
	data = [int(x) for x in inp[1].split(' ')]

	ans = sol(target, data)

	if len(ans) == 0:
		print("No Subset")
		return

	for i in range(len(ans)):
		ans[i] = ascending_sort(ans[i])

	ans = sort_sol(ans)

	for i in ans:
		print(i)

if __name__ == '__main__':
	main()