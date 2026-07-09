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
	width, height, room = input('Enter width, height, and room: ').split(' ')
	width, height = int(width), int(height)
	room_map = room.split(',')

	if len(room_map) != height or any(len(r) != width for r in room_map) or not any('F' in r for r in room_map):
		print("Invalid map input.")
		return

	start = next(((x, y) for y, row in enumerate(room_map) for x, char in enumerate(row) if char == 'F'), None)

	q = Queue()
	q.enqueue(start)
	visited = {start}

	directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

	while len(q) > 0:
		print(f"Queue: {q.items}")
		curr_x, curr_y = q.dequeue()

		for dx, dy in directions:
			nx, ny = curr_x + dx, curr_y + dy

			if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
				cell = room_map[ny][nx]

				if cell == 'O':
					print("Found the exit portal.")
					return
				elif cell == '_':
					q.enqueue((nx, ny))
					visited.add((nx, ny))

	print("Cannot reach the exit portal.")

if __name__ == '__main__':
	main()