print("Welcome to Manga Recommender")
print("\n1. Horror")
print("2. Action")
print("3. Romance")
genre = input ("\nWhat genre of manga do you want: ")

if genre == "1":
	duration = input("How long do you want (short/medium/long): ")
	if duration.lower() == "short":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We recommend Nightmares for Sale")
		elif year == "2010s":
			print("We recommend Dissolving Classroom")
		else:
			print("\nPlease select again")		
	elif duration.lower() == "medium":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We recommend Dragon Head")
		elif year == "2010s":
			print("We recommend I Am a Hero")
		else:
			print("\nPlease select again")
	elif duration.lower() == "long":
		year = input("What year do you prefe (2000s/2010s):")
		if year == "2000s":
			print("We recommend MPD Psycho")
		elif year == "2010s":
			print("We recommend Kasane")
	else: 
		print("\nPlease select again")			
elif genre == "2":
	duration = input("How long do you want (short/medium/long): ")
	if duration.lower() == "short":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We recommend Blame! Academy and So On")
		elif year == "2010s":
			print("We recommend All You Need Is Kill")
		else:
				print("\nPlease select again")
	elif duration.lower() == "medium":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We recommend Black Cat")
		elif year == "2010s":
			print("We recommend Akame ga Kill!")
		else:
				print("\nPlease select again")
	elif duration.lower() == "long":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We recommend Eyeshield 21")
		elif year == "2010s":
			print("We recommend Attack on Titan")	
		else: 
			print("\nPlease select again")
	else:
		print("\nPlease select again")
elif genre == "3":
	duration = input("How long do you want (short/medium/long): ")
	if duration.lower() == "short":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We recommend Orange Chocolate")
		elif year == "2010s":
			print("We recommend My Little Monster")
		else:
			print("\nPlease select again")
	elif duration.lower() == "medium":
		year = input("What year do you prefer (2000s/2010s):")
		if year == "2000s":
			print("We recommend Absolute Boyfriend")
		elif year == "2010s":
			print("We recommend Ao Haru Ride")
		else:
			print("\nPlease select again")
	elif duration.lower() == "long":
		year = input("What year do you prefe (2000s/2010s):")
		if year == "2000s":
			print("We recommend Marmalade Boy")
		elif year == "2010s":
			print("We recommend Kimi ni Todoke: From Me to You")	
		else:
			print("\nPlease select again")
	else:
		print("\nPlease select again")
else:

	print("\nPlease select again")


