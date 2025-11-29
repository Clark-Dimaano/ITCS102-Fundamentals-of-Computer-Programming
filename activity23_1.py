def GreetWithName(name):
    print(f"Hi {name}, Hope you have splendid day")

def Funtionwithreturn(number):
    print(f"This function calculates the summation from 1 to {number}")
    sum = 0
    for x in range(1,number + 1,1):
        sum += x
    return sum

def factorial(number):
    print(f"This funtion calculate the factorial from {number} to 1")
    fact = 1    
    for x in range(number, 0, -1):
        fact *= x
    return fact

def triangle():
    for i in range(1,11):
        for x in range(10,i,-1):
            print(" ", end = " ")
        for y in range(1,i):
            print("*", end = " ")
        for z in range(1,i):
            print("*", end = " ")
        print()
    
