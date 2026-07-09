class Queue:
	def __init__(self, items=None):
		if items is None:
			self.items = []
		else:
			self.items = items

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def __len__(self):
		return len(self.items)

def main():
	q = Queue()
	data = input('Enter Input : ').split(',')

	for c in data:
		c = c.split(' ')
		action = c[0]

		if action == 'E':
			number = c[1]
			q.enqueue(number)
			print(f'Add {number} index is {len(q) - 1}')
		elif action == 'D':
			try:
				number = q.dequeue()
				print(f'Pop {number} size in queue is {len(q)}')
			except IndexError:
				print('-1')
	if len(q) == 0:
		print('Empty')
	else:
		print(f'Number in Queue is :  {q.items}')

if __name__ == '__main__':
	main()