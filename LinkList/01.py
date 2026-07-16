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
		now = self.head
		while now != None:
			str_repres += str(now.data)
			str_repres += "->"
			now = now.next
		if len(str_repres) > 1:
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

def print_lst(lst: LinkList):
	if lst.isEmpty():
		print('List is empty')
	else:
		print(f'link list : {lst}')

def main():
	lst = LinkList()
	inp = input('Enter Input : ').split(',')
	initial = inp[0]
	cmds = inp[1:]
	initial = initial.split(' ')
	for _, item in enumerate(initial):
		try:
			lst.append(int(item.strip()))
		except:
			pass
	print_lst(lst)
	for _, cmd in enumerate(cmds):
		cmd = cmd.strip()
		index, item = cmd.split(':')
		index = int(index)
		item = int(item)
		if index < 0 or index > len(lst):
			print('Data cannot be added')
			print_lst(lst)
			continue
		lst.insert(index, item)
		print(f'index = {index} and data = {item}')
		print_lst(lst)

if __name__ == '__main__':
	main()