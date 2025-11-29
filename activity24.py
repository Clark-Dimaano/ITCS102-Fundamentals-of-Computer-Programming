from activity23_1 import *

print("WELCOME TO MY COMPILER PROGRAM ")
name = input("Hi Visitor, what is your name --> ")

print(f"Hi {name}, select from the optons below ")
print("A - Greet name,\nB - Greet wtih Name, Age, Location\nC - Triangle\nE - Exit ")

isCpmt = True

while isCpmt == True:
    choice = input("Select a letter from A - E --> ").lower()

    if choice == 'a':
        GreetWithName(name)
        continue
    elif choice == 'b':
        pass
    elif choice == 'c':
        triangle()
        continue
    elif choice == 'e':
        break

    else:
        print("Invalid choice")
        continue
        
