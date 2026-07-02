def hbd(age):
	### Enter Your Code Here ###
	base21 = (age - 1) / 2
	base20 = (age) / 2
	if base21.is_integer():
		return f"saimai is just 21, in base {int(base21)}!"
	elif base20.is_integer():
		return f"saimai is just 20, in base {int(base20)}!"

year = input("Enter year : ")
print(hbd(int(year)))