import os

name = input("Hello user, please input your name: ").title()
print(f"Hi {name}, welcome to code compiler")


yn = input("\nWould you like to use my code compiler? (yes/no): ")
while True:  
    
    if yn == 'yes':
        print("=================================================")
        print("A - Functions ")
        print("B - Escape Sequence")
        print("C - If/Elif Else")
        print("D - List and Dictionary")
        print("X - Exit Menu")
        
        
        select = input("Select what command should we run: ").lower()
        
        if select == 'a':
            print("1 - Built-in Function") 
            print("2 - User-Defined Function ")
            x = input("Input the function should we use: ")
            if x == '1':
                print("=====================================================================================")
                print("Here are some of the function and its use:")
                print("\nprint() -    Displays text, numbers, or variables on the screen.\n             It’s the most commonly used function for showing program output.")
                print("               Example: ")
                print("               name = 'Alice'")
                print("               age = 25")
                print("               print('Name:', name, 'Age:', age)")
                print("\n               Output: ")
                print("               Name: Alice, Age: 25 ")
            elif x == '2':
                pass
            else:
                print("Select again")
                continue
        elif select == 'x':
            print("You have exited the program")
            break
             

    elif yn == 'no':
        print("Thanks for using it")
        break
    else:
        print("Invalid Choice, try again")
        continue
