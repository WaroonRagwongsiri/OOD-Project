def sort_count(data):
	hash_map = {}
	for i in data:
		if i in hash_map.keys():
			hash_map[i] += 1
		else:
			hash_map[i] = 1

	seen = []
	for i in data:
		if (i, hash_map[i]) in seen:
			continue
		seen.append((i, hash_map[i]))

	for i in range(len(seen)):
		for j in range(len(seen) - i - 1):
			if seen[j][1] < seen[j + 1][1]:
				tmp = seen[j]
				seen[j] = seen[j + 1]
				seen[j + 1] = tmp

	return seen

def main():
	inp = input('Enter list  of numbers: ').split(' ')
	inp = [int(x) for x in inp]
	data = sort_count(inp)
	for i in data:
		print(f'number {i[0]}, total: {i[1]}')

if __name__ == '__main__':
	main()