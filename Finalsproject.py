
import os

name = input("Hello user, please input your name: ").title()

print(f"Welcome {name}, here are the menu for code compiler: ")

while True:  
        print("=================================================")
        print("A - Functions ")
        print("B - Escape Sequence")
        print("C - If/Elif Else")
        print("D - List and Dictionary")
        print("X - Exit Menu")
        print("=================================================")

                
        
        select = input("Select what command should we run: ").lower()
        if select == 'a':
             
        
            while True:                                                                                    
                print("============================================================================")
                
                    
                print("1 - Built-in Function") 
                print("2 - User-Defined Function")
                print("X - Back")
                print("============================================================================")
                
                x = input("Input the function should we use: ")
                
                                                                                
                if x == '1':
                    os.system('cls')
                    print("===================================================================")                                                                
                    print("1 - Definitions\n2 - Run the code")
                    print("===================================================================")
                  
                    y = input("Input your choice: ")
                                                        
                    os.system('cls')
                    if y == '1':
                        print("=====================================================================================")
                        print("Here are some of the function and its use:")
                        print("\nprint() -    Displays text, numbers, or variables on the screen.\n             It’s the most commonly used function for showing program output.")
                        print("               Example: ")
                        print("               name = 'Alice'")
                        print("               age = 25")
                        print("               print(\"Name:\", name, \"Age:\", age)")
                        print("\n               Output: ")
                        print("               Name: Alice, Age: 25 ")
                        print("\ninput() -    This function allows the program to take input from the user as a string.\n             You can provide a prompt inside the parentheses to guide the user.\n\t     If you need a number, you usually convert the input using int() or float().")
                        print("               Example: ")
                        print("               age = input(\"Enter your age: \")")
                        print("               print(\"You are\", age, \"years old\")")
                        print("\n               Output (if the user enters 20):")
                        print("               Enter your age: 20 ")
                        print("               You are 20 years old")
                        print("\nrange() -    This function generates a sequence of numbers. It is commonly used in for loops. \n\t     You can specify a start, stop, and step value. It does not create a list in memory, which makes it memory-efficient.\n\t       Example:\n\t       for i in range(1,6,1):\n\t           print(i)\
                        \n\n\t       Output:\n\t       1\n\t       2\n\t       3\n\t       4\n\t       5")
                        print("\neval() -    This function takes a string argument containing a valid expression, evaluates it, and returns the result of that expression. \n\t    It can evaluate numbers, arithmetic expressions, lists, tuples, function calls, and more.\n\t       Example:\n\t       x = 3\n\t       y = 4\n\t       print(eval(x * y))\n\n\t     Output:\n\t       12")
                        print("\nlen() -     Returns the number of items in a collection: for example, characters in a string, elements in a list/tuple/dictionary/set, etc.\n\t    It works for any object that defines a length (i.e. implements the “sequence” or “collection” interface).")
                        print("\t     Example:\n\t     x = \"Hello\"")   
                        print("\t     print(len(x))")                    
                        print("\n\t     Output:")  
                        print("\t     5")     
                        print("=====================================================================================")
                        

                                
                    
                        input("Press any key to go back: ")                                                    
                        os.system('cls')
                        continue
                    elif y == '2':
                        print("=====================================================================================")

                        name = 'Alice'
                        age = 20
                        print("Name:", name, ",Age:", age)

                        age = input("\nEnter your age: ")
                        print(f"Your age is {age} years old\n")
                        print("\n====================================\n(for i in range(1,6,1):)\n\t(print(i))")
                        for i in range(1,6,1):
                            print(i)
                        print("====================================")
                
                        print("\nx * y = \nInput a number to multiply:")              
                        x = eval(input("x = "))
                        y = eval(input("y = "))
                        ans = x * y 
                        print(f"\nThe answer from what you input is {ans}")
                        print("=====================================================================================")
                        input("Press any key to go back: ")
                        continue        
                                                                                                                    
                elif x == 'x':                                                        
                    print("Back to menu")
                    break              
                elif  x == '2':
                        
                        
                    print("===================================================================")
                    print("1 - Definition\n2 - Run the code")
                    print("===================================================================")
                    y = input("Input your choice: ")
                    if y == '1':
                        print("=====================================================================================")               
                        print("The user-defined function is a set of instructions that you create to do a specific job. Instead of writing the same code again and again, you make a function once and call it whenever you need it. You create a function using the (def) keyword, give it a name, and write the code you want it to run\nBasic Structure:\ndef functiuon_name():\n    # code to run")
                        print("=====================================================================================")
                        input("Press any key to go back: ") 

                    elif y == '2':
                        print("====================================")
                        def greet( ):
                            print("Hello! Wellcome to the Python.")
                    
                        print("\nCode:\n def greet( ):\n    print(\"Hello! Welcome to the Python.\")\n greet( )\n\nOuput:")
                        greet()
                        print("\n====================================")
                        input("press any key to go back: ")
                                               
                else:
                    os.system('cls')
                    print("Select again")
                
        elif select == 'b':
            print("===================================================================")
            print("1 - Definition/descriptions\n2 - Examples")
            print("===================================================================")
            x = input("Input your choice: ")
            if x == '1':
                print("The escape sequence is the sequence of characters that starts with a backslash (`\\`) and is used to represent special, non‑printable, or control characters inside a string. The backslash tells the interpreter/compiler to interpret the following character(s) differently from its literal meaning.")
                print("\nHere are the common types of escape sequence:")
                print("  Sequence        Meaning\n    \\n          New line\n    \\t          Horizontal tab\n    \\r          Carriage reuturn (back to start of line\n    \\\\          Literal backslash\n    \\\'          Single quote '\n    \\\"          Double quote \"\n    \\b          Backspace")
                      
            elif x == '2':
                      
                print("Examples:")          
                print("\n1.print(\"Hello\\nWorld\")")
                print("\nOutput:")
                print("Hello\nWorld")
                print("\n2.print(\"Name:\\tJohn\")")
                print("\nOutput:")
                print("Name:\tJohn")
                print("\n3.print(\"Hello\\rWorld\")")
                print("\nOutput:")
                print("Hello\rWorld")
                print("\n4.print(\"C:\\\\Users\\\\User\")")
                print("\nOutput:")
                print("C:\\Users\\User")
                print("\n5.print(\"It\\\'s Python\")")
                print("\nOutput:")
                print("It\'s Python")     
                print("\n6.print(\"\\\"Quote\\\"\")")          
                print("\nOutput:")           
                print("\"Quote\"")
                print("\n7.print(\"123\\b4\")")
                print("\nOutput:")
                print("123\b4")
        elif select == 'x':               
                print("You have exited  the program")
                break

        else:                                                                                                                      
                print("Invalid Choice, try again")     
                continue
