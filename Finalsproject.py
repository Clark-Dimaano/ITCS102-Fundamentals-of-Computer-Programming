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
            print("============================================================================")
            print("1 - Built-in Function") 
            print("2 - User-Defined Function ")
            x = input("Input the function should we use: ")

            if x == '1':
                print("===================================================================")
                print("1 - Definitions\n2 - Run the code")
                y = input("Input your choice: ")
                if y == '1':
                    print("=====================================================================================")
                    print("Here are some of the function and its use:")
                    print("\nprint() -    Displays text, numbers, or variables on the screen.\n             It’s the most commonly used function for showing program output.")
                    print("               Example: ")
                    print("               name = 'Alice'")
                    print("               age = 25")
                    print("               print('Name:', name, 'Age:', age)")
                    print("\n               Output: ")
                    print("               Name: Alice, Age: 25 ")
                    print("\ninput() -    This function allows the program to take input from the user as a string.\n             You can provide a prompt inside the parentheses to guide the user. If you need a number, you usually convert the input using int() or float().")
                    print("               Example: ")
                    print("               age = input('Enter your age: ')")
                    print("               print('You are', age, 'years old')")
                    print("\n               Output (if the user enters 20):")
                    print("               Enter your age: 20 ")
                    print("               You are 20 years old")
                    print("\nRange() -    This function generates a sequence of numbers. It is commonly used in for loops. \n\t     You can specify a start, stop, and step value. It does not create a list in memory, which makes it memory-efficient.\n\t       Example 1 (simple loop):\n\t       for i in range(1,6,1):\n\t           print(i)\
                        \n\n\t       Output:\n\t       1\n\t       2\n\t       3\n\t       4\n\t       5")
                elif y == 2:
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
