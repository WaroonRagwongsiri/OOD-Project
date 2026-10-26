class HashTable:
	def __init__(self, size, max_col, threshold):
		self.size = int(size)
		self.max_col = int(max_col)
		self.threshold = int(threshold)
		self.table = [None] * self.size
		self.items = []

	def is_prime(self, n):
		if n < 2:
			return False
		for i in range(2, int(n ** 0.5) + 1):
			if n % i == 0:
				return False
		return True

	def next_prime(self, n):
		curr = n * 2 + 1
		while not self.is_prime(curr):
			curr += 1
		return curr

	def _insert(self, key):
		for i in range(self.max_col):
			idx = (key + i ** 2) % self.size
			if self.table[idx] is None:
				self.table[idx] = key
				return True
			else:
				print(f"collision number {i + 1} at {idx}")
		return False

	def rehash(self):
		self.size = self.next_prime(self.size)
		self.table = [None] * self.size
		for item in self.items:
			self._insert(item)

	def add(self, key):
		print(f"Add : {key}")

		# 1. Check if adding this element exceeds the threshold
		if (len(self.items) + 1) * 100 / self.size >= self.threshold:
			print("****** Data over threshold - Rehash !!! ******")
			self.rehash()

		# 2. Try inserting; if max collisions reached, rehash and retry
		while not self._insert(key):
			print("****** Max collision - Rehash !!! ******")
			self.rehash()

		self.items.append(key)
		self.print_table()

	def print_table(self):
		for i, val in enumerate(self.table):
			print(f"#{i + 1}\t{val}")
		print("----------------------------------------")


def main():
	print(" ***** Rehashing *****")
	initial, items = input("Enter Input : ").split("/")
	initial = initial.strip().split()
	items = [int(x) for x in items.strip().split()]

	hash_table = HashTable(initial[0], initial[1], initial[2])
	print("Initial Table :")
	hash_table.print_table()

	for item in items:
		hash_table.add(item)


if __name__ == "__main__":
	main()