def main():
	print(' *** Trap Water *** ')
	user_input = input('Input heights : ')
	height = [int(x) for x in user_input.split(' ')]

	total_water = 0

	for i, now in enumerate(height):
		L = max(height[:i+1])
		R = max(height[i:])

		total_water += min(L, R) - now

	print(f'Trapped Water: {total_water}')

if __name__ == '__main__':
	main()
