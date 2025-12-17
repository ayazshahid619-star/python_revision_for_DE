temp = int (input("enter temperature:"))
unit = (input("enter unit in F or C only:"))

if unit == "F":
	print((temp-32)*5/9)
elif unit == "C":
	print((temp*(9/5))+32)
else:
	print("Invalid Entry: Enter only F or C")
	
