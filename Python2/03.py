class TorKham:
	def __init__(self):
		self.words = []
		self.last = None

	def restart(self):
		### Enter Your Code Here ###
		self.words = []
		self.last = None

		return "game restarted"

	def play(self, word):
		### Enter Your Code Here ###
		if self.last == None:
			self.last = word
			self.words.append(word)
			return self.words
		if self.last[-2:].lower() != word[:2].lower():
			return "game over"
		self.last = word
		self.words.append(word)
		return self.words

torkham = TorKham()

print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')

### Enter Your Code Here ###
for index, item in enumerate(S):
	if item == 'X':
		break
	elif item == 'R':
		print(torkham.restart())
		continue
	elif item[:2] != 'P ':
		print(f"'{item}' is Invalid Input !!!")
		break
	word = item[2:]
	print(f"'{word}' -> {torkham.play(word)}")