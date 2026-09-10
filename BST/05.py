class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.val)

class BST:
	def __init__(self, implicit_bst_array=None):
		self.root = self.build_tree(implicit_bst_array, 0)

	def build_tree(self, arr, index):
		if not arr or index >= len(arr) or arr[index] is None:
			return None

		node = Node(arr[index])
		node.left = self.build_tree(arr, 2 * index + 1)
		node.right = self.build_tree(arr, 2 * index + 2)

		return node

	def isvalid(self):
		def check_valid(node, lower=None, upper=None):
			if node is None:
				return True

			if lower is not None and node.val <= lower:
				return False

			if upper is not None and node.val >= upper:
				return False

			return (
				check_valid(node.left, lower, node.val)
				and
				check_valid(node.right, node.val, upper)
			)

		return check_valid(self.root)

	def merge_add(self, tree):
		if not tree or not tree.root:
			print("\nCannot merge these trees.")
			return

		def search_leaf(root, val):
			if not root:
				return None

			if root.left:
				matched_node = search_leaf(root.left, val)
				if matched_node: return matched_node

			if root.right:
				matched_node = search_leaf(root.right, val)
				if matched_node: return matched_node

			if not root.left and not root.right:
				if root.val == val:
					return root

			return None

		matched_node = search_leaf(self.root, tree.root.val)
		
		if matched_node:
			matched_node.left = tree.root.left
			matched_node.right = tree.root.right

			if self.isvalid():
				print("\nMerged successfully:")
				self.print_tree(self.root)
				return

		print("\nCannot merge these trees.")

	def print_tree(self, node, level=0):
		if not node:
			return
		self.print_tree(node.right, level + 1)
		print("    " * level + str(node.val))
		self.print_tree(node.left, level + 1)

def main():
	t1_str, t2_str = input("Enter trees: ").split(" / ")

	t1_str = t1_str.strip()[1:-1].split(",")
	t2_str = t2_str.strip()[1:-1].split(",")

	tree1 = [None if i.strip().lower() == "null" or not i.strip() else int(i.strip()) for i in t1_str]
	tree2 = [None if i.strip().lower() == "null" or not i.strip() else int(i.strip()) for i in t2_str]

	T1 = BST(tree1)
	T2 = BST(tree2)

	T1.merge_add(T2)

if __name__ == '__main__':
	main()