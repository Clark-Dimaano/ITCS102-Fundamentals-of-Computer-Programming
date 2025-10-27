import random 

print("\nNUMBER GUESSING GAME")
print("\n+++++++++++++++++++++++++++")

random_value = random.randint(1,5)
tries = 0 
tuloy = True

name = input("\nInput your nanme -->  ")

while tuloy == True:
    num = eval(input("Guess number from 1 to 5 -->  "))
    tries += 1
    if num == random_value:
        print("Winner !!!!")
        break
    else:
        print("Incorrect Guess")
        continue

print(f"Hi {name}, Your guess in correct, Number of tries {tries}")