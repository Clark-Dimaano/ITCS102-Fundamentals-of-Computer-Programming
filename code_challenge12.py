for i in range(1,7,1):
	for y in range(7,i,-1):
		print(" ", end = " ")
	for x in range(i,1,-1):
		print(x, end = " ")
	for z in range(1,i + 1):
		print(z, end =" ")
	print()

