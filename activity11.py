temp = eval(input("Input is the temperature outside --> "))

if temp <= 0:
	print("Temperature is hazardly cold")
elif temp >= 1 and temp <= 20:
	print("Temperature is Extremely cold")
elif temp > 20 and temp <= 30:
	print("Temperature is cold")
elif temp > 30 and temp <= 37:
	print("Temperature is lukewarm")
elif temp > 37 and temp <= 45:
	print("Temperature is hot")
elif temp > 45 and temp <= 50:
	print("Temperature is boilling hot")
elif temp> 50:
	print("Temperature is dangarous")
else:
	print("Temperature invalid")