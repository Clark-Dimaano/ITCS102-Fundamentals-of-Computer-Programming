print("Welcome to Manga Reccomender")
print("\n1. Horror")
print("2. Action")
print("3. Romance")
genre = input ("\nWhat genre of manga do you want: ")

if genre == "1":
	duration = input("How long do you want (short/medium/long): ")
	if duration.lower() == "short":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We reccomend Nightmares for Sale")
		elif year == "2010s":
			print("We reccomend Dissolving Classroom")
		else:
			print("\nPlease select again")		
	elif duration.lower() == "medium":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We reccomend Dragon Head")
		elif year == "2010s":
			print("We reccomend I Am a Hero")
		else:
			print("\nPlease select again")
	elif duration.lower() == "long":
		year = input("What year do you prefe (2000s/2010s)")
		if year == "2000s":
			print("We reccomend MPD Psycho")
		elif year == "2010s":
			print("We reccomend Kasane")
	else: 
		print("\nPlease select again")			
elif genre == "2":
	duration = input("How long do you want (short/medium/long): ")
	if duration.lower() == "short":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We reccomend Blame! Academy and So On")
		elif year == "2010s":
			print("We reccomend All You Need Is Kill")
		else:
				print("\nPlease select again")
	elif duration.lower() == "medium":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We reccomend Black Cat")
		elif year == "2010s":
			print("We reccomend Akame ga Kill!")
		else:
				print("\nPlease select again")
	elif duration.lower() == "long":
		year = input("What year do you prefer (2000s/2010s)")
		if year == "2000s":
			print("We reccomend Eyeshield 21")
		elif year == "2010s":
			print("We reccomend Attack on Titan")	
		else: 
			print("\nPlease select again")
	else:
		print("\nPlease select again")
elif genre == "3":
	duration = input("How long do you want (short/medium/long): ")
	if duration.lower() == "short":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We reccomend Orange Chocolate")
		elif year == "2010s":
			print("We reccomend My Little Monster")
		else:
			print("\nPlease select again")
	elif duration.lower() == "medium":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We reccomend Absolute Boyfriend")
		elif year == "2010s":
			print("We reccomend Ao Haru Ride")
		else:
			print("\nPlease select again")
	elif duration.lower() == "long":
		year = input("What year do you prefe (2000s/2010s)")
		if year == "2000s":
			print("We reccomend Marmalade Boy")
		elif year == "2010s":
			print("We reccomend Kimi ni Todoke: From Me to You")	
		else:
			print("\nPlease select again")
	else:
		print("\nPlease select again")
else:

	print("\nPlease select again")
