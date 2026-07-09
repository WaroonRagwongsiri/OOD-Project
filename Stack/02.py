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

	def size(self):
		return len(self.items)

main_stack = Stack()

def ManageStack(command: str):
	parts = command.split(' ')
	cmd = parts[0]

	if cmd == 'A':
		number = int(parts[1])
		main_stack.push(number)
		print(f'Add = {number}')

	elif cmd == 'P':
		if main_stack.isEmpty():
			print('-1')
		else:
			print(f'Pop = {main_stack.pop()}')

	elif cmd == 'D':
		if main_stack.isEmpty():
			print('-1')
			return

		number = int(parts[1])
		temp_stack = Stack()

		while not main_stack.isEmpty():
			val = main_stack.pop()
			if val == number:
				print(f'Delete = {val}')
			else:
				temp_stack.push(val)

		while not temp_stack.isEmpty():
			main_stack.push(temp_stack.pop())

	elif cmd == 'LD':
		if main_stack.isEmpty():
			print('-1')
			return

		number = int(parts[1])
		temp_stack = Stack()

		while not main_stack.isEmpty():
			val = main_stack.pop()
			if val < number:
				print(f'Delete = {val} Because {val} is less than {number}')
			else:
				temp_stack.push(val)

		while not temp_stack.isEmpty():
			main_stack.push(temp_stack.pop())

	elif cmd == 'MD':
		if main_stack.isEmpty():
			print('-1')
			return

		number = int(parts[1])
		temp_stack = Stack()

		while not main_stack.isEmpty():
			val = main_stack.pop()
			if val > number:
				print(f'Delete = {val} Because {val} is more than {number}')
			else:
				temp_stack.push(val)
		while not temp_stack.isEmpty():
			main_stack.push(temp_stack.pop())

if __name__ == "__main__":
	commands = input('Enter Input : ').split(',')

	for c in commands:
		ManageStack(c)

	print(f"Value in Stack = {main_stack.items}")