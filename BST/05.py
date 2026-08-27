class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def __len__(self):
		return len(self.items)

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return f"Node({self.data})"

class BST:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root == None:
			self.root = Node(data)
			return self.root

		current = self.root
		while True:
			if data < current.data:
				if current.left == None:
					current.left = Node(data)
					break
				current = current.left
			else:
				if current.right == None:
					current.right = Node(data)
					break
				current = current.right

		return self.root

	def insert_specific(self, key, data):
		current = self.root
		while current is not None:
			if current.data == key:
				break
			elif key < current.data:
				current = current.left
			else:
				current = current.right

		if current is None:
			return

		while True:
			if data < current.data:
				if current.left == None:
					current.left = Node(data)
					break
				current = current.left
			else:
				if current.right == None:
					current.right = Node(data)
					break
				current = current.right


	def findDepth(self, node, key, depth = 0):
		if node == None:
			return -1

		if node.data == key:
			return depth

		if key < node.data:
			return self.findDepth(node.left, key, depth + 1)
		else:
			return self.findDepth(node.right, key, depth + 1)

	def bfs_traverse(self):
			q = Queue()
			output = []
			q.enqueue(self.root)
			while len(q) != 0:
				current = q.dequeue()
				output.append(current.data)
				if current.left:
					q.enqueue(current.left)
				if current.right:
					q.enqueue(current.right)
			return output

	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     ' * level, node)
			self.printTree(node.left, level + 1)

	def is_identical(node1, node2):
		if node1 is None and node2 is None:
			return True
		if node1 is None or node2 is None:
			return False

		if node1.data == node2.data:
			return BST.is_identical(node1.left, node2.left) and BST.is_identical(node1.right, node2.right)

		return False

def main():
	T1 = BST()
	T2 = BST()

	t1, t2 = input('Enter trees: ').split('/')

	t1 = eval(t1.replace('null', 'None'))
	t2 = eval(t2.replace('null', 'None'))

	for i in t1:
		if i == None:
			continue
		T1.insert(i)
		T2.insert(i)

	print('')

	if len(t2) == 0:
		return

	root_t2 = t2[0]
	t2 = t2[1:]

	found = T1.findDepth(T1.root, root_t2)
	if found == -1:
		print('Cannot merge these trees.')
		return

	for i in t2:
		if i == None:
			continue
		T1.insert_specific(root_t2, i)
		T2.insert(i) 

	# Check Tree
	if not BST.is_identical(T1.root, T2.root):
		print('Cannot merge these trees.')
		return

	print('Merged successfully:')
	T1.printTree(T1.root)

if __name__ == '__main__':
	main()
