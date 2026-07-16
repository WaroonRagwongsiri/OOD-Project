class Node:
	def __init__(self, data):
		self.data = data
		self.next: Node | None = None

class CircularLinkedList:
	def __init__(self):
		self.head: Node | None = None

	def append(self, data):
		new_node = Node(data)
		if self.head == None:
			new_node.next = new_node
			self.head = new_node
		else:
			current = self.head
			while current.next != self.head:
				current = current.next
			current.next = new_node
			new_node.next = self.head

	def insert(self, target_data, ins_data):
		if self.head is None:
			raise ValueError("List is empty")

		current = self.head
		while True:
			if current.data == target_data:
				new_node = Node(ins_data)
				new_node.next = current.next
				current.next = new_node
				return
			
			current = current.next
			if current == self.head:
				break

		raise ValueError(f"Not found: {target_data}")

	def delete(self, data):
		if self.head is None:
			raise ValueError("List is empty")

		if self.head.data == data:
			if self.head.next == self.head:
				self.head = None
			else:
				last_node = self.head
				while last_node.next != self.head:
					last_node = last_node.next

				self.head = self.head.next
				last_node.next = self.head
			return

		current = self.head
		while current.next != self.head:
			if current.next.data == data:
				current.next = current.next.next
				return
			current = current.next

		raise ValueError(f"Not found: {data}")

	def shift(self, k: int):
		for i in range(k):
			self.head = self.head.next

	def __str__(self):
		if not self.head:
			return "Empty"

		str_rep = ""
		current = self.head
		while True:
			str_rep += str(current.data)
			str_rep += " "
			current = current.next
			if current == self.head:
				break
		str_rep = str_rep[:-1]
		return str_rep

def main():
	lst = CircularLinkedList()

	inp = input(':>').split(' ')
	for index, item in enumerate(inp):
		if item == 'A':
			lst.append(int(inp[index + 1]))
		elif item == 'I':
			try:
				lst.insert(int(inp[index + 1]), int(inp[index + 2]))
			except ValueError as e:
				print(e)
		elif item == 'D':
			try:
				lst.delete(int(inp[index + 1]))
			except ValueError as e:
				print(e)
		elif item == 'R':
			lst.shift(int(inp[index + 1]))
		elif item == 'P':
			print(lst)
		elif item == 'E':
			break

if __name__ == '__main__':
	main()
