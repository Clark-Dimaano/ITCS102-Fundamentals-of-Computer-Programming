col = eval(input("Enter a number for column --> "))
    
for i in range(1,11):
    for x in range(1,col + 1):
        ans = i * x 
        print(f"{i} x {x} = {ans}\t", end=" ")
    print()

for i in range(1,6,1):
    for x in range(6,i,-1):
        print(" ", end="")
    for y in range(1,i+1):
        print("* ",end="")
    print()