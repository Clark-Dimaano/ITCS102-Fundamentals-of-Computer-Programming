temp = eval(input("Enter temperature outside --> "))

if temp <= 0:
	print("Temperature is considered as freezling cold")
elif temp >= 1 and temp <= 20:
	print("Temperature is considered as extremely cold")
elif temp > 20 and temp <= 30:
	print("Temperature is considered as cold")
elif temp > 30 and temp <= 37:
	print("Temperature is considered as lukewarm")
elif temp > 37 and temp <= 45:
	print("Temperature is comsidered as hot")
elif temp > 45 and temp <= 50:
	print("Temperature is considered as boilling hot")
elif temp > 50:
	print("Temperature is considered as dangerous temperature")
else:
	print("Temperature Invalid")