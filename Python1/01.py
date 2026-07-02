def main():
	print("*** Converting hh.mm.ss to seconds ***")
	try:
		t = input("Enter hh mm ss : ")
		hh, mm, ss = t.split(' ')
		hh = int(hh)
		mm = int(mm)
		ss = int(ss)
		if mm > 59 or mm < 0:
			raise Exception(f"mm({mm}) is invalid!")
		if ss > 59 or ss < 0:
			raise Exception(f"mm({ss}) is invalid!")
		sec = hh * 60 * 60 + mm * 60 + ss
		print(f"{hh:02}:{mm:02}:{ss:02} = {sec:,} seconds")
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()