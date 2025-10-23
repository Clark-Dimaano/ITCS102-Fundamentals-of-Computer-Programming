
Tunay = True
list = [ ]

while Tunay == True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ").lower()
  
    if anime != 'exit':
        print(f"'{anime}' has been added to your anime list.")
        list.append(anime)
        continue

    	
	
    elif anime == 'exit':
        print("You have exited the anime enrty program.")
        break

    else:
        print("Please try again")

print("\nYour anime list includes:")
for anime in list:
	print(f"- {anime}")

