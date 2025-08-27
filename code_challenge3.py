name = input("Please enter your name --> ")
fare = eval(input("Input your fare --> "))
ifstudent = input("Are you a student (yes / no) ")

if ifstudent.lower() == "yes":
	discount = fare *  0.2
	new_fare = fare - discount
	print("Hi", name, "your discount is", discount, "and your new fare is", new_fare)
else: 
	print("Hi", name,"your fare is stil",  fare)