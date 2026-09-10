class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1

	def __str__(self):
		return str(self.data)

class AVL:
	def __init__(self):
		self.root = None

	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     ' * level, node)
			self.printTree(node.left, level + 1)

	def height(self, node): 
		if node == None:
			return 0
		return node.height

	def get_balance(self, node):
		if node == None:
			return 0
		return self.height(node.left) - self.height(node.right)

	def right_rotate(self, root):
		new_root = root.left
		moving_tree = new_root.right 

		new_root.right = root
		root.left = moving_tree

		root.height = 1 + max(self.height(root.left), self.height(root.right))
		new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))

		return new_root

	def left_rotate(self, root):
		new_root = root.right
		moving_tree = new_root.left 

		new_root.left = root
		root.right = moving_tree

		root.height = 1 + max(self.height(root.left), self.height(root.right))
		new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))

		return new_root

	def rebalance(self, root):
		root.height = 1 + max(self.height(root.left), self.height(root.right))
		balance = self.get_balance(root)

		# Left Heavy Tree
		if balance > 1:
			if self.get_balance(root.left) < 0: 
				root.left = self.left_rotate(root.left)
			return self.right_rotate(root)

		# Right Heavy Tree
		elif balance < -1:
			if self.get_balance(root.right) > 0: 
				root.right = self.right_rotate(root.right)
			return self.left_rotate(root)

		return root

	def insert(self, data):
		self.root = self.insert_node(self.root, data)

	def insert_node(self, root, data):
		if root == None:
			return Node(data)
		elif data < root.data:
			root.left = self.insert_node(root.left, data) 
		elif data >= root.data:
			root.right = self.insert_node(root.right, data) 
		else:
			return root

		return self.rebalance(root)

def max_sum_traverse(root):
	if root == None:
		return ""

	path = ""
	max_sum = 0
	current = root

	while current != None:
		max_sum += current.data
		path += str(current.data)

		if current.right:
			current = current.right
			path += " + "
		elif current.left:
			current = current.left
			path += " + "
		else:
			current = None

	return path, max_sum

def main():
	T = AVL()

	inp = input('Enter tree nodes: ').strip().split(' ')

	for i in inp:
		i = int(i)

		T.insert(i)

	T.printTree(T.root)
	print()
	path, max_sum = max_sum_traverse(T.root)
	print(f'Path with maximum sum: {path} = {max_sum}')

if __name__ == '__main__':
	main()