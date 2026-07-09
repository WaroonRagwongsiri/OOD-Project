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
	data = input('Enter Input : ').split(',')
	my_q = Queue()
	yu_q = Queue()

	act_dict = {'0': 'Eat', '1': 'Game', '2': 'Learn', '3': 'Movie'}
	loc_dict = {'0': 'Res.', '1': 'ClassR.', '2': 'SuperM.', '3': 'Home'}

	for day in data:
		my_data, yu_data = day.split(' ')
		my_q.enqueue(my_data)
		yu_q.enqueue(yu_data)

	print(f'My   Queue = {", ".join(my_q.items)}')
	print(f'Your Queue = {", ".join(yu_q.items)}')

	my_mapped = []
	yu_mapped = []
	score = 0

	while len(my_q) > 0:
		my_curr = my_q.dequeue()
		yu_curr = yu_q.dequeue()

		my_act, my_loc = my_curr.split(':')
		yu_act, yu_loc = yu_curr.split(':')

		my_mapped.append(f"{act_dict[my_act]}:{loc_dict[my_loc]}")
		yu_mapped.append(f"{act_dict[yu_act]}:{loc_dict[yu_loc]}")

		if my_act == yu_act and my_loc == yu_loc:
			score += 4
		elif my_act == yu_act and my_loc != yu_loc:
			score += 1
		elif my_act != yu_act and my_loc == yu_loc:
			score += 2
		else:
			score -= 5

	print(f'My   Activity:Location = {", ".join(my_mapped)}')
	print(f'Your Activity:Location = {", ".join(yu_mapped)}')

	if score >= 7:
		print(f"Yes! You're my love! : Score is {score}.")
	elif score > 0:
		print(f"Umm.. It's complicated relationship! : Score is {score}.")
	else:
		print(f"No! We're just friends. : Score is {score}.")

if __name__ == '__main__':
	main()