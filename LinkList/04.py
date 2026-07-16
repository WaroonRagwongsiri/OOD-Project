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
			str_repres += "->"
			now = now.next

		str_repres = str_repres[:-2]
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

def find_loop(lst: LinkList) -> bool:
	founded = []
	current = lst.head
	while current != None:
		if current in founded:
			return True
		founded.append(current)
		current = current.next
	return False

def main():
	inp = input('Enter input : ').split(',')

	lst = LinkList()

	for i in inp:
		action, data = i.split(' ')
		if action == 'A':
			lst.append(int(data))
			print(lst)
			
		elif action == 'S':
			idx1, idx2 = data.split(':')
			idx1 = int(idx1)
			idx2 = int(idx2)

			if lst.isEmpty():
				print('Error! {list is empty}')
				continue

			if idx1 < 0 or idx1 >= len(lst):
				print(f'Error! {{index not in length}}: {idx1}')
				continue

			if idx2 < 0 or idx2 >= len(lst):
				lst.append(idx2)
				print(f'index not in length, append : {idx2}')
				continue

			node1, node2 = lst.set_point(idx1, idx2)
			print(f'Set node.next complete!, index:value = {idx1}:{node1.data} -> {idx2}:{node2.data}')
			
	loop = find_loop(lst)
	if loop:
		print('Found Loop')
	else:
		print('No Loop')
		print(lst)

if __name__ == '__main__':
	main()