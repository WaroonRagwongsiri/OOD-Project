class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def __len__(self):
		return len(self.items)

class Stack:
	def __init__(self, items=None):
		if items is None:
			self.items = []
		else:
			self.items = items

	def push(self, i):
		self.items.append(i)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0

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

	def __str__(self):
		return self.print_tree(self.root, 0)

	def print_tree(self, node, level = 0):
		if node is None:
			return ""
		result = self.print_tree(node.right, level + 1)
		result += " " * 4 * level + f"{node.data}\n"
		result += self.print_tree(node.left, level + 1)
		return result

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

	def bfs_traverse_pisadarn(self):
		s = Stack()
		output = []
		s.push(self.root)
		while len(s) != 0:
			current = s.pop()
			output.append(current.data)
			if current.left:
				s.push(current.left)
			if current.right:
				s.push(current.right)
		return output


def main():
	T = BST()
	print('******BFS Pis-sa-dan******')
	numbers = [int(i) for i in input('Enter numbers: ').split()]
	for i in numbers:
		root = T.insert(i)
	print(T)
	bfs = T.bfs_traverse()
	bfs_pis = T.bfs_traverse_pisadarn()
	print(f'BFS: {bfs}')
	print(f'BFS Pid-Sa-Dan: {bfs_pis}')


if __name__ == '__main__':
	main()