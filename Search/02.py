class Shelf:
	def __init__(self, book = None, counter = None):
		if book == None:
			self.book = []
		else:
			self.book = book

		if counter == None:
			self.counter = []
		else:
			self.counter = counter

	def search(self, key):
		if key in self.counter:
			self.counter.remove(key)
			self.book.insert(0, key)
			return 1, f"Search {key} -> add new book ->  {' '.join(self.book)}"

		index = 1
		for index, item in enumerate(self.book):
			if key == item:
				moving = self.book.pop(index)
				self.book.insert(0, moving)
				return index + 1, f"Search {key} -> found at {index + 1} move to front ->  {' '.join(self.book)}"

		self.counter.append(key)
		return index + 2, f"Search {key} -> not found -> {' '.join(self.book)}"

def main():
	print('This is your BOOK!!!')
	books, search = input('Enter input: ').split('/')
	books = books.split(' ')
	search = search.split(' ')
	shelf = Shelf(books)
	total_cost = 0
	for index, item in enumerate(search):
		cost, msg = shelf.search(item)
		print(msg)
		total_cost += cost
	print()
	print(f"Final books: {' '.join(shelf.book)}")
	print(f"Total cost: {total_cost}")

if __name__ == '__main__':
	main()