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

def main():
	T = BST()
	print('***Range Sum***')

	l, low, high = input('Enter input : ').split('/')

	numbers = [int(i) for i in l.split()]
	low = int(low)
	high = int(high)

	seen = set()
	for i in numbers:
		if i not in seen:
			root = T.insert(i)
			seen.add(i)

	print('')
	print('Binary Search Tree:')
	T.printTree(root)
	print('')

	print(f'Range : [{low}, {high}]')

	bfs = T.bfs_traverse()
	sum = 0
	for i in bfs:
		if i >= low and i <= high:
			sum += i
	print(f'Sum of nodes in range = {sum}')


if __name__ == '__main__':
	main()