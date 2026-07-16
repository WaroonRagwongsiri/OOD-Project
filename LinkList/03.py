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

	def tail(self):
		if self.head == None:
			return None

		now = self.head
		while now.next != None:
			now = now.next
		return now

def count_merge(lst):
	found_merges = [] 

	for branch1 in lst:
		curr1 = branch1.head

		while curr1 is not None and curr1.next is not None:
			for branch2 in lst:
				curr2 = branch2.head

				while curr2 is not None and curr2.next is not None:

					if curr1.data == curr2.data and curr1.next.data != curr2.next.data:
						if curr1.data not in found_merges:
							found_merges.append(curr1.data)

					curr2 = curr2.next

			curr1 = curr1.next
	return len(found_merges)


def main():
	branches = input('Git History: ').split('|')
	for index, branch in enumerate(branches):
		branch = branch.split('->')
		branch_lst = LinkList()
		for commit in branch:
			branch_lst.append(int(commit.strip()))
		branches[index] = branch_lst

	b = branches[0].tail().data
	same = True
	for branch in branches:
		if branch.tail().data != b:
			same = False
	print(f'Are these branches in the same repository? {same}')
	if same:
		merge_cnt = count_merge(branches)
		print(f'{merge_cnt} Merge(s)')


if __name__ == '__main__':
	main()