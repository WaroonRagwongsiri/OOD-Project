class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def __len__(self):
		return len(self.items)

def main():
	user_input = input("Enter code,hint : ").split(',')
	code = user_input[0]
	hint = user_input[1]

	q = Queue()

	shift = ord(code[0]) - ord(hint)

	for char in code:
		decoded_ascii = ord(char) - shift

		decoded_char = chr(decoded_ascii)

		q.enqueue(decoded_char)
		print(q.items)

if __name__ == '__main__':
	main()