print("ODD NUMBER ACCUMULATOR \nEnter 10 numbers. We'll sum inly the odd ones!")
sum = 0
for x in range(1, 11):
    number = eval(input("Enter number: "))
    if number % 2 != 0:  
        sum += number  
print("\n\tSum of all odd numbers:", sum)
    
    