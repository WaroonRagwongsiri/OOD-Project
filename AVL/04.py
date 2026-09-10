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

def game_traverse(root, health):
	if root == None:
		return ""

	path = ""
	current = root

	while current != None:
		health -= current.data
		path += str(current.data)

		if health <= 0:
			break

		if current.left:
			current = current.left
			path += " -> "
		elif current.right:
			current = current.right
			path += " -> "
		else:
			current = None

	if health > 0:
		print('SUCCESS!')
		print(f'Remaining HP : {health}')
	else:
		print('GAME OVER!')
		print(f'Died Node : {current.data}')
		print(f'HP at death : {health}')
	print(f'Path : {path}')

def main():
	T = AVL()

	inp = input('Enter Input : ').strip().split('/')

	if len(inp) < 2: 
		print('EMPTY DUNGEON!')
		return

	tree_inp = inp[0].split() 
	health = int(inp[1].strip())

	if not tree_inp:
		print('EMPTY DUNGEON!')
		return

	for i in tree_inp:
		T.insert(int(i))

	game_traverse(T.root, health)

if __name__ == '__main__':
	main()