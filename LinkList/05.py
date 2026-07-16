class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def __len__(self):
		return len(self.items)

	def is_empty(self):
		return not len(self)

class Node:
	def __init__(self, data):
		self.data = data
		self.next: Node = None

class LinkList:
	def __init__(self):
		self.head: Node | None = None
		self.size = 0

	def __str__(self):
		str_repres = ""

		if len(self) == 0:
			return "Empty"

		now = self.head
		while now != None:
			str_repres += str(now.data)
			str_repres += " -> "
			now = now.next

		str_repres = str_repres[:-4]
		return str(str_repres)

	def __len__(self):
		size = 0
		now = self.head
		while now != None:
			size += 1
			now = now.next
		return size

	def isEmpty(self):
		size = 0
		now = self.head
		if now != None:
			return False
		return True

	def append(self, data):
		now = self.head
		if now == None:
			self.head = Node(data)
			return
		while now.next != None:
			now = now.next
		now.next = Node(data)

	def insert(self, index, data):
		if index > len(self) or index < 0:
			raise IndexError("Index out of bound")

		new = Node(data)

		if index == 0:
			new.next = self.head
			self.head = new
			return

		now = self.head
		for _ in range(index - 1):
			now = now.next

		new.next = now.next
		now.next = new

	def tail(self):
		if self.head == None:
			return None

		now = self.head
		while now.next != None:
			now = now.next
		return now

	def node_index(self, index):
		if index < 0 or index >= len(self):
			raise ValueError('Index out of bound')
		node = self.head
		for i in range(index):
			node = node.next
		return node

	def set_point(self, idx1: int, idx2: int):
		if idx1 < 0 or idx1 >= len(self):
			raise ValueError('Index out of bound')

		node1 = self.node_index(idx1)

		node2 = self.node_index(idx2)

		node1.next = node2
		return (node1, node2)

	def __iter__(self):
		now = self.head
		while now is not None:
			yield now.data
			now = now.next

def get_digit(number):
    if number == 0:
        return 0

    number = abs(number)

    digit = 1
    while number // 10 > 0:
        digit += 1
        number //= 10
    return digit

def get_digit_at_position(number, position):
	return (abs(number) // (10 ** position)) % 10

def radix_sort(numbers, max_digits):
	digit_queues = [Queue() for _ in range(10)]

	for position in range(max_digits):
		print('------------------------------------------------------------')
		print(f'Round : {position + 1}')

		for number in numbers:
			if number < 0:
				digit = get_digit_at_position(number, position)
				digit_queues[digit].enqueue(number)

		for number in numbers:
			if number >= 0:
				digit = get_digit_at_position(number, position)
				digit_queues[digit].enqueue(number)

		for i, queue in enumerate(digit_queues):
			row_str = f"{i} :"
			for val in queue.items: 
				row_str += f" {val}"
			print(row_str)

		numbers = LinkList()

		for i in range(9, -1, -1):
			for val in digit_queues[i].items:
				if val < 0:
					numbers.append(val)

		for i in range(10):
			while not digit_queues[i].is_empty():
				val = digit_queues[i].dequeue()
				if val >= 0:
					numbers.append(val)

	return numbers

def main():
	values = input('Enter Input : ').split( )
	before = LinkList()
	after = LinkList()

	for index, item in enumerate(values):
		values[index] = int(item)
		before.append(int(item))

	max_digit = max(get_digit(max(values)), get_digit(min(values)))

	after = radix_sort(before, max_digit)
	print('------------------------------------------------------------')
	print(f'{max_digit} Time(s)')
	print(f'Before Radix Sort : {before}')
	print(f'After  Radix Sort : {after}')

if __name__ == '__main__':
	main()