CAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOW = "abcdefghijklmnopqrstuvwxyz"

class funString():
	def __init__(self,string = ""):
		### Enter Your Code Here ###
		self.string = string

	def __str__(self):
		### Enter Your Code Here ###
		return str(self.string)

	def size(self) :
		### Enter Your Code Here ###
		return len(self.string)

	def changeSize(self):
		### Enter Your Code Here ###
		new = ""
		for index, item in enumerate(self.string):
			if item in CAP:
				new += LOW[CAP.find(item)]
			elif item in LOW:
				new += CAP[LOW.find(item)]
		return new

	def reverse(self):
		### Enter Your Code Here ###
		return self.string[::-1]

	def deleteSame(self):
		### Enter Your Code Here ###
		new = ""
		for index, item in enumerate(self.string):
			if item in new:
				continue
			new += item
		return str(new)

str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())
