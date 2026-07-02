def main():
	print("*** Fun with countdown ***")
	l = input('Enter List : ').split(' ')
	ans = []
	last = None
	for index, item in enumerate(l):
		l[index] = int(l[index])
	for index, item in enumerate(l):
		if item == 1:
			count = []
			for j in range(index, -1, -1):
				now = l[j]
				if last != None and now != last + 1:
					break
				count.append(now)
				last = now
			count.reverse()
			ans.append(list(count))
			last = None
	sol = [len(ans), ans]
	print(sol)

if __name__ == '__main__':
	main()