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
	peoples, time = input('Enter people and time : ').split(' ')
	main_queue = Queue()
	cashier1 = Queue()
	cashier2 = Queue()

	c1_time_spent = 0
	c2_time_spent = 0

	time = int(time)

	for p in peoples:
		main_queue.enqueue(p)

	for i in range(1, time + 1):
		if c1_time_spent == 3:
			cashier1.dequeue()
			c1_time_spent = 0

		if c2_time_spent == 2:
			cashier2.dequeue()
			c2_time_spent = 0

		if len(main_queue) > 0:
			if len(cashier1) < 5:
				cashier1.enqueue(main_queue.dequeue())
			elif len(cashier2) < 5:
				cashier2.enqueue(main_queue.dequeue())

		if len(cashier1) > 0:
			c1_time_spent += 1
			
		if len(cashier2) > 0:
			c2_time_spent += 1

		print(f'{i} {main_queue.items} {cashier1.items} {cashier2.items}')

if __name__ == '__main__':
	main()