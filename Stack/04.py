class Stack:
	def __init__(self, items=None):
		if items is None:
			self.items = []
		else:
			self.items = items

	def push(self, i):
		self.items.append(i)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

def main():
	S = Stack()

	inp = input('Enter Input : ').split(',')

	for c in inp:
		c = c.split(' ')
		action = c[0]
		if action == 'A':
			number = int(c[1])
			S.push(number)
		elif action == 'B':
			# peak
			temp = Stack()
			max_height = None
			cnt = 0
			while not S.isEmpty():
				now = S.pop()
				temp.push(now)
				if max_height == None:
					max_height = now
					cnt += 1
					continue
				if max_height >= now:
					continue
				max_height = now
				cnt += 1
			while not temp.isEmpty():
				S.push(temp.pop())
			print(cnt)


if __name__ == '__main__':
	main()