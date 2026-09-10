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
			print("*")
			return self.root

		path = ""
		current = self.root
		while True:
			if data < current.data:
				path += "L"
				if current.left == None:
					current.left = Node(data)
					break
				current = current.left
			else:
				path += "R"
				if current.right == None:
					current.right = Node(data)
					break
				current = current.right

		path += "*"
		print(path)
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

def main():
	T = BST()
	inp = input('Enter Input : ').strip().split(' ')
	root = None
	for i in inp:
		root = T.insert(int(i))
		# print()
		# T.printTree(root)

if __name__ == '__main__':
	main()
