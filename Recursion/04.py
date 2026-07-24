def find_start(grid: list):
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == 'S':
				return (r, c)
	return None

def find_end(grid: list):
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == 'E':
				return (r, c)
	return None

def is_valid(grid: list, pos: tuple):
	r, c = pos

	if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
		return False

	if grid[r][c] in ['#', '*', 'S']:
		return False

	return True

def dfs(grid: list, pos: tuple, start: tuple, end: tuple):
	r, c = pos

	if pos == end:
		return True

	original_char = grid[r][c]

	if grid[r][c] != 'S':
		grid[r][c] = '*'

	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	for dr, dc in directions:
		new_pos = (r + dr, c + dc)

		if is_valid(grid, new_pos):
			if dfs(grid, new_pos, start, end):
				return True

	grid[r][c] = original_char
	return False

def parse_maze(maze_str: str):
	maze_str = maze_str.upper()
	rows = maze_str.split(',')
	grid = [list(row) for row in rows]
	return grid

def print_grid(grid: list):
	for row in grid:
		print("".join(row))

def main():
	print("Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.")
	print("Separate each row with a comma (,).")
	maze_inp = input('Enter the maze: ').strip()

	print('Your maze:')
	grid = parse_maze(maze_inp)
	print_grid(grid)

	start = find_start(grid)
	end = find_end(grid)

	if start and end:
		success = dfs(grid, start, start, end)
		if success:
			print('Solution found:')
			print_grid(grid)
		else:
			print("No solution found")
	else:
		print("No solution found")

if __name__ == '__main__':
	main()