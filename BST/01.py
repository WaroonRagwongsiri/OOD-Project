class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
	def __str__(self):
		return str(self.data)

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


	def findDepth(self, node, key, depth = 0):
		if node == None:
			return -1

		if node.data == key:
			return depth

		if key < node.data:
			return self.findDepth(node.left, key, depth + 1)
		else:
			return self.findDepth(node.right, key, depth + 1)

	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     ' * level, node)
			self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
values = inp[:-1]
key = inp[-1]

for i in values:
	root = T.insert(i)
T.printTree(root)
print('-' * 50)
print(f"Depth of {key} : {T.findDepth(root, key)}")