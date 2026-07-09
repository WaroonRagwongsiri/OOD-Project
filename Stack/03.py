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

def game(stack, c):
	action, number = c.split(' ')
	action = str(action)
	number = int(number)
	if action.lower() == 'spawn':
		stack.push(number)
		print(f'spawn an enemy of {number} HP')
	elif action.lower() == 'dmg':
		dmg = number
		if dmg <= 0:
			print('Invalid number')
			return
		enemy = None
		die = 0
		while dmg > 0:
			initial_dmg = dmg
			try:
				enemy = stack.pop()
			except IndexError:
				break
			dmg -= enemy
			enemy -= initial_dmg
			if enemy <= 0:
				die += 1
		if enemy > 0:
			stack.push(enemy)
		print(f'deal {number} damage, killed {die} enemy')
	print(stack.items)
	print()

def main():
	initial_stack, commands = input('Enter Input : ').split('/')
	initial_stack = initial_stack.split(' ')
	if initial_stack[0] == '':
		initial_stack = []
	for index, item in enumerate(initial_stack):
		initial_stack[index] = int(item)
	initial_stack = [item for item in initial_stack if item > 0]
	commands = commands.split(',')
	stack = Stack(initial_stack)
	print()
	print('start')
	print(stack.items)
	print()
	for c in commands:
		game(stack, c)
	if stack.isEmpty():
		print(">>>> Player Wins <<<<")

if __name__ == '__main__':
	main()
