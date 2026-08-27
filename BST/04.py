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

def print_path(path, suffix):
	print(f'{suffix} ', end='')
	print(' -> '.join(str(x) for x in path))

def solve(node, treasure, escape, f_treasure, path):
	if node.data == treasure:
		print('Found Treasure !!!')
		f_treasure = True 

	if node.data == escape:
		if f_treasure:
			print('Found Escape !!!')
			print_path(path, '✅')
			return True

	print_path(path, '❌')

	if node.left is not None:
		if solve(node.left, treasure, escape, f_treasure, path + [node.left.data]):
			return True

	if node.right is not None:
		if solve(node.right, treasure, escape, f_treasure, path + [node.right.data]):
			return True

	return False

def main():
	T = BST()

	numbers, treasure, escape = input('Enter Input : ').split('/')

	numbers = [int(inp) for inp in numbers.split()]
	treasure = int(treasure)
	escape = int(escape)

	for i in numbers:
		root = T.insert(i)

	T.printTree(root)
	print('-------------------------------------------------')

	if root is not None:
		success = solve(root, treasure, escape, False, [root.data])

		if success:
			print('>>> Mission Complete <<<')
		else:
			print('>>> Mission Failed <<<')

if __name__ == '__main__':
	main()
