
import os

name = input("Hello user, please input your name: ").title()
os.system('cls')

print(f"Welcome {name}, here are the menu for code compiler: ")

while True:  
        print("====================MENU====================")
        print("\tA - Functions ")
        print("\tB - Escape Sequence")
        print("\tC - Conditional Statement")
        print("\tD - Data Structure")
        print("\tX - Exit Menu")
        print("============================================")

                
        
        select = input("Select what command should we run: ").lower()
        os.system('cls')
        if select == 'a':
             
        
            while True:                                                                                    
                print("===============FUNCTION===============")                   
                print("\t1 - Built-in Function") 
                print("\t2 - User-Defined Function")
                print("\t0 - Back")
                print("======================================")
                
                x = input("Input the function should we use: ")
                
                                                                                
                if x == '1':
                    while True:                                                                                    
                        os.system('cls')
                        print("===============BUILT-IN FUNCTION===============")                                                                
                        print("\t1 - Definitions\n\t2 - Run the code\n\t0 - Back")
                        print("===============================================")
                  
                        y = input("Input your choice: ")
                        os.system('cls')
                                                        
                        if y == '1':
                            print("===============================================DEFINITIONS===============================================")
                            print("Here are some of the function and its use:")
                            print("\nprint() -    Displays text, numbers, or variables on the screen. It’s the most commonly used function for\n             showing program output.")
                            print("               Example: ")
                            print("               name = 'Alice'")
                            print("               age = 25")
                            print("               print(\"Name:\", name, \"Age:\", age)")
                            print("\n               Output: ")
                            input("               Name: Alice, Age: 25 ")
                            print("\ninput() -    This function allows the program to take input from the user as a string. You can provide a\n             prompt inside the parentheses to guide the user. If you need a number, you usually convert\n             the input using int() or float().")
                            print("               Example: ")
                            print("               age = input(\"Enter your age: \")")
                            print("               print(\"You are\", age, \"years old\")")
                            print("\n               Output (if the user enters 20):")
                            print("               Enter your age: 20 ")
                            input("               You are 20 years old")
                            input("\nrange() -    This function generates a sequence of numbers. It is commonly used in for loops. You can\n             specify a start, stop, and step value. It does not create a list in memory, which makes\n             it memory-efficient.\n\t       Example:\n\t       for i in range(1,6,1):\n\t           print(i)\
                        \n\n\t       Output:\n\t       1\n\t       2\n\t       3\n\t       4\n\t       5")
                            input("\neval() -    This function takes a string argument containing a valid expression, evaluates it, and\n            returns the result of that expression. It can evaluate numbers, arithmetic expressions,\n             lists, tuples, function calls, and more.")
                            print("\t\tOperators\t\tName\t\t\tDescription")
                            print("\t\t+\t\tAddition\t\tAdds two values together")
                            print("\t\t-\t\tSubtraction\t\tSubstract right value from left value")
                            print("\t\t*\t\tMultiplication\t\tMultiplies two values (a * b)")
                            print("\t\t/\t\tDivision\t\tDivides left by right returning a float (a / b) ")
                            print("\t\t//\t\tFloor Division\t\tDivides and returns the integer part (a // b)")
                            print("\t\t%\t\tModulus(Remainder)\tReturns the remainder of division (a % b)")
                            input("\t\t**\t\tExponentiation\t\tRaises left value to the power of right (a ** b)")
                            input("\n\t\t       Example:\n\t\t       x = 3\n\t\t       y = 4\n\t\t       print(eval(x * y))\n\n\t\t     Output:\n\t\t       12")
                            print("\nlen() -     Returns the number of items in a collection: for example, characters in a string, elements \n            in a list/tuple/dictionary/set, etc.\n\t    It works for any object that defines a length (i.e. implements the “sequence” or\n             “collection” interface).")
                            print("\t     Example:\n\t     x = \"Hello\"")   
                            print("\t     print(len(x))")                    
                            print("\n\t     Output:")  
                            print("\t     5")  
                            print("=========================================================================================================")       
                            input("Press any key to go back: ")                                                    
                            os.system('cls')
                            continue
                            
                        elif y == '2':
                            print("============================RUN THE CODE============================")
                            print("print():")
                            print("name = \"Alice\"")
                            print("age = 20")
                            print("\nOutput:")
                            Name = 'Alice'
                            age = 20
                            print("Name:", Name, " ,Age:", age)
                            input("")

                            print("\ninput()")
                            age = input("Enter your age: ")
                            print(f"Your age is {age} years old\n")
                            print("\nin range():")
                            x = eval(input("Welcome space ranger, enter a number to start the countdown: "))
                            for i in range(x, 0, -1):
                                print(i)
                            print("\nLiftoff!!!!!")
                            
                            print("\neval()")
                            print("Input a number to multiply:\nx * y = \n")              
                            x = eval(input("x = "))
                            y = eval(input("y = "))
                            ans = x * y 
                            print(f"\nThe product from what you input is {ans}")
                            print("====================================================================")
                            input("Press any key to go back: ")
                            os.system('cls')
                            continue 

                        elif y == '0':   
                            os.system('cls')
                            break    

                        else:
                            os.system('cls')
                            
                                                                                                                    
                elif x == '0':                                                        
                    print("Back to menu")
                    os.system('cls')
                    break          

                elif  x == '2':
                    while True:   
                        os.system('cls')                   
                        print("===============USER DEFINED FUNCTION===============")
                        print("\t1 - Definition\n\t2 - Example\n\t0 - Back")
                        print("===================================================")
                        y = input("Input your choice: ")
                        os.system('cls')

                        if y == '1':
                            print("===============================================DEFINITION===============================================")               
                            print("The user-defined function is a set of instructions that you create to do a specific job. Instead of\nwriting the same code again and again, you make a function once and call it whenever you need it. You\ncreate a function using the (def) keyword, give it a name, and write the code you want it to run\n\nBasic Structure:\ndef functiuon_name():\n    # code to run")
                            print("========================================================================================================")
                            input("Press any key to go back: ")
                            os.system('cls')

                        elif y == '2':
                            print("============================EXAMPLE============================")
                            def greet( ):
                                print("Hello! Wellcome to the Python.")                  
                            print("\nCode:\n def greet( ):\n    print(\"Hello! Welcome to the Python.\")\n greet( )\n\nOuput:")
                            greet()
                            print("\n=============================================================")
                            input("press any key to go back: ")
                            os.system('cls')
                        
                        elif y =='0':
                            print("Back to menu")
                            os.system('cls')
                            break                  
                else:
                    os.system('cls')
                    print("Select again")
                
        elif select == 'b':
            while True:
                print("===============ESCAPE SEQUENCE===============")
                print("1 - Definition/descriptions\n2 - Examples\n0 - Back")
                print("=============================================")
                x = input("Input your choice: ")
                os.system('cls')
                
                if x == '1':
                    print("===============================================DEFINITION/DESCRIPTION===============================================")
                    print("The escape sequence is the sequence of characters that starts with a backslash (`\\`) and is used to\nrepresent special, non‑printable, or control characters inside a string. The backslash tells the\ninterpreter/compiler to interpret the following character(s) differently from its literal meaning.")
                    input("\nHere are the common types of escape sequence:")
                    print("  Sequence        Meaning\n    \\n          New line\n    \\t          Horizontal tab\n    \\r          Carriage reuturn (back to start of line\n    \\\\          Literal backslash\n    \\\'          Single quote '\n    \\\"          Double quote \"\n    \\b          Backspace")
                    print("====================================================================================================================")  
                    input("press any key to go back: ")
                    os.system('cls')

                elif x == '2':
                    print("===============================================EXAMPLES===============================================")
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
                    print("=========================================================================================================")
                    input("press any key to go back: ")
                    os.system('cls')
                
                elif x == '0': 
                    print("Back to menu")
                    os.system('cls')
                    break

        elif select == 'c':
            while True:
                print("=====================CONDITIONAL STATEMENTS=========================")
                print("\t1 - If/Elif & Else")
                print("\t2 - Loops")
                print("\t0 - Back")
                print("====================================================================")
                x = input("Input your choice: ") 
                os.system('cls')

                if x == '1':
                    while True:
                        os.system('cls')
                        print("=====================IF/ELIF & ELSE=========================")
                        print("\t1 - Definition")
                        print("\t2 - Try the code")
                        print("\t0 - Back")
                        print("============================================================")
                        y = input("Input your choice: ")
                        os.system('cls')
                        
                        if y == '1':
                            print("===============================================DEFINITION===============================================")
                            input("It is a conditional statement that lets your program make decisions — choose between different blocks of\ncode — depending on whether specified conditions are met or not. In Python, the main keywords used\nfor this are if, elif, and else.")
                            print("\nRoles of if/elif/else:")
                            input("if —   This is the basic conditional. When Python reaches an if, it evaluates the expression (condition)\n       that follows. If that condition evaluates to True, the code block under if executes;\n       if it’s False, Python skip that block.")
                            input("\nelif -   Short for “else if.” This is used when you want to check additional conditions, but only in the\n          case where the previous if  or earlier elif  evaluated to False. You can have zero or more elif \n          clauses after an if. As soon as one elif condition is found to be True, its block executes, and \n          the rest of the chain (further elifs or else) is skipped")
                            input("\nelse -   This is the “fallback” or “default” block. It has no condition. It runs only if all previous if\n         and elif conditions in the chain were False. The else clause is optional — you can omit it if you\n         don’t need a default action.")
                            print("\nBasic Structure:")
                            print("if condition1:\n\t# code block executed if condition1 is True")
                            print("elif condition2:\n\t# code block executed if condition1 is False and condition2 is True")
                            print("elif condition3:\n\t# code block executed if previous conditions are False and condition3 is True")
                            print("else:\n\t# code block executed if none of the above conditions are True")
                            print("========================================================================================================")
                            input("Press any key to go back: ")
                            os.system('cls')

                        elif y == '2':
                            print("================================TRY THE CODE================================")
                            print("If you put more that 30, it will print a message that says \"It\'s a hot day!\"\nand if you put 30 to 20 it will print \"It\' a nice day.\" \nand if you put 20 to 10 it will print \"It\'s a bit chilly.\", \nbut if you put below 10 it will print \"It\'s cold.")
                            print("\nLet\'s try it:")
                            x = eval(input("What\'s the temperature today --> "))

                            if x > 30:
                                print("It's a hot day!")
                            elif x <= 30 and x >= 20:
                                print("It's a nice day.")
                            elif x >= 10 and x < 20:
                                print("It's a bit chilly.")
                            else:
                                print("It's cold.")
                            print("====================================================================")
                            input("Press any key to go back: ")
                            os.system('cls')

                        elif y == '0':
                            break


                elif x == '2':
                    while True:
                        print("=====================LOOPS==================================")
                        print("\t1 - Definition")
                        print("\t2 - Examples")
                        print("\t0 - Back")
                        print("============================================================")
                        y = input("Input your choice: ")

                        if y == '1':
                            print("===============================================DEFINITION===============================================")
                            input("A loop is a control‑flow structure that allows a program to repeat a block of code multiple times. \nInstead of writing the same code over and over manually, you write it once inside a loop, and the loop \nhandles the repetition.Loops are especially useful when you have a sequence of data (like a list or \nstring) to process, or when you want to repeat a task until a certain condition is met.")
                            input("\nTypes of loop:")
                            input("for loop -   is used to iterate over a sequence (like a list, tuple, string, or range) or any iterable object. \n             Use afor loop when you know in advance that you want to process every element in a collection, \n             or when you know exactly how many times you want to repeat something (e.g. using range(...)).")
                            input("\nwhile loop -   loop repeats a block of code as long as a condition remains true. Before each iteration, \n               Python checks the condition; if it's True, it runs the block; if it's False, it exits the loop.")
                            input("\nBasic Structure:")
                            print("for loop:")
                            print("for variable in sequence:")
                            print("\t# code block (body of the loop)")
                            print("\nwhile loop:")
                            print("while condition:")
                            print("\t# code block (body of the loop)")
                            print("========================================================================================================")
                            input("Press any key to go back: ")
                            os.system('cls')
                        
                        elif y == '2':
                            fruits = ["apples", "banana", "avocado"]
                            print("============================EXAMPLES============================")
                            print("for loop:")
                            print("fruits = [\"apple\", \"banana\", \"avocado\"]")
                            print("for x in fruits:")
                            print("\tprint(f\"I like the fruit {x})")
                            print("\nOutput:")
                            for x in fruits:
                                print(f"I like the fruit {x}")
                            print("\nwhile loop:")
                            print("if you keep chossing yes, it will continue but if you choose no, it will stop.")
                            print("Let\'s try it:\n")
                            while True:
                                x = input("Would you like to continue this code (yes/no): ").lower()

                                if x == 'yes':
                                    continue
                                elif x == 'no':
                                    print("The loop has been stop.....")
                                    break
                                else:
                                    print("Please answer correctly")
                                    continue
                            print("================================================================")
                            input("Press any key to go back: ")
                            os.system('cls')
                            
                        elif y == '0':
                            os.system('cls')
                            break   


                elif x == '0':
                    os.system('cls')
                    break

                elif x == '0':
                    while True:
                        break

        elif select == 'd':
            while True:
                print("===============DATA STRUCTURE===============")
                print("\t1 - Definition")
                print("\t2 - Examples")
                print("\t0 - Back")
                print("============================================")
                x = input("Enter your choice: ")
                os.system('cls')

            
                if x == '1':
                    print("===============================================DEFINITION===============================================")
                    input("A data structure is a way to store, organize, and manage data so that you can access, modify, and \nmanipulate it efficiently.")
                    input("\nTypes of data structure:")
                    input("list -   An ordered, mutable collection of items (which can be of mixed types). You can access items by \n         index (0, 1, 2, ...), add, remove or change items, and the list size can grow or shrink. Good \n         when you need a dynamic collection of elements.")          
                    input("\ndictionary -   A collection of key → value pairs (mapping). Keys must be unique and (usually) of \n               immutable types; values can be anything. Useful when you want to map identifiers to data — \n               for example, mapping names to ages, or IDs to records")
                    print("========================================================================================================")   
                    input("Press any key to go back: ")
                    os.system('cls')

                elif x == '2':
                    
                    def operation():   
                        print("===============================================EXAMPLE===============================================")
                        print("Here are the common list operations:")
                        print("\tOperation\t\t\tSyntax\t\t\t\tDescription\t\t")
                        print("\tAppend\t\t\tlist.insert(index,item)\t\tAdds an item to the end")
                        print("\tInsert\t\t\tlist.insert(index,item)\t\tInsert item at specified index")
                        print("\tRemove\t\t\tlist.remove(index)\t\tRemoves first occurence of item")
                        print("\tpop\t\t\tlist.pop(index)\t\t\tRemoves and returns item at index")
                        print("\tsort\t\t\tlist.sort()\t\t\tSorts the list(ascending by default)")
                        print("\tLength\t\t\tlen(list)\t\t\tReturns number of elements")
                        print("\tReverse\t\t\tlist.reverse()\t\t\tReverse the list order")
                        print("\nLet\'s try it:")
                  
                    prutas = []
                      
                     
                    while True:
                        operation()
                        print("list.apped():")                                               
                        fruit = input("Add any fruit that you like --> ")   
                        prutas.append(fruit)
                        print(f"\nList = {prutas}")
                        
                        con = input("Continue?: ")
                        if con == 'yes':
                            os.system('cls')
                            pass
                        
                        elif con == 'no':
                            os.system('cls')
                            break



                    # print("\nInsert():")
                    ins = ["mango","apple","banana"]
                    # print("List = [\"mango\",\"apple\",\"banana\"]") 
                    # print("            0      1        2")    
                    operation()
                    print("\ninsert():")
                    print("fruit = [\"mango\",\"apple\",\"banana\"]") 
                    print("            0      1        2")    
                    while True:
                       
                        
                        
            
                        y = input("Input the fruit you want to add: ")
                        z = eval(input("Where should we put it: "))
                        ins.insert(z,y)
                        
                        print(f"\nfruit = {ins}")
                        

                        con = input("\nContinue?: ")
                        if con == 'yes':
                            os.system('cls')
                            operation()
                            print("\nInsert():")

                        elif con == 'no':
                            os.system('cls')
                            break

                    operation()
                    print("\nremove():")
                    print("color = [\"red\",\"blue\",\"yellow\",\"orange\"]")
                    
                    color = ["red","blue","yellow","orange"]
                    while True:
                        
                    
                           
                            
                        x = input("What color should we remove?: ")
                        color.remove(x)

                        print(f"\ncolor = {color}")

                        con = input("\nContinue?: ")
                        if con =='yes':
                            os.system('cls')
                            operation()
                            print("\nremove():")
                            print(f"\ncolor = {color}")
                            
                            
                        elif con == 'no':
                            os.system('cls')
                            break

                    food = ["sinigang","adobo","kare-kare"]

                    operation()
                    print("\npop():")
                    print("food = [\"sinigang\",\"adobo\",\"kare-kare\"]")
                    print("           0          1         2") 
                    
                    while True:
                        

                        x = eval(input("Input here the index that you want to pop: "))
                        food.pop(x)
                        print(f"food = {food}")

                        con = input("\nContinue?: ")
                        if con == 'yes':
                            print(f"food = {food}")

                            

                        elif con == 'no':
                            os.system('cls')
                            break
                             
                    num = []
                    
                    while True:
                        operation()
                        print("list.sort():")
                        x = input("Enter a random numbers: ")
                        num.append(x)
                        print(f"number = {num}")
                        

                        con = input("\nContinue?: ")
                        if con == 'yes':
                            os.system('cls')

                        elif con == 'no':
                            print("\nHere are the sorted number that you input:")
                            num.sort()
                            print(f"number = {num}")
                            input("")
                            os.system('cls')
                            break
                    
                    numero = []
                    operation()
                    print("list.reverse():")
                    while True:
                        x = eval(input("Enter a random number: "))
                        numero.append(x)
                        print(f"number = {numero}")

                        more = input("\nAdd more?: ")
                        if more == 'yes':
                            os.system('cls')
                            operation()
                            print("list.reverse():")

                        elif more == 'no':
                            print("\nHere are the reversed number that you input:")
                            numero.reverse()
                            print(f"number = {numero}")
                            input("")
                            os.system('cls')
                            break
                    
                    operation()
                    print("\nlist.length():")
                    numbers = []
                    while True:
                        x = input("Input a random number: ")
                        numbers.append(x)
                        print(f"numbers = {numbers}")

                        more = input("\nAdd more?: ")
                        if more == 'yes':
                            os.system('cls')
                            operation()
                            print("\nlist.length():")

                        elif more == 'no':
                            print("\nHere is the length of the numbers that you input:")
                            print(len(numbers))
                            break

                    print("=====================================================================================================")
                    input("Press any key to go back: ")
                    os.system('cls')
    
                elif x == '0':
                    os.system('cls')
                    break
        elif select == 'x':  
                os.system('cls')           
                print("You have exited the program")                
                break

        else:
                os.system('cls')                                                                                                                      
                print("Invalid Choice, try again")                     
                continue
