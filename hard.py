loan = eval(input("Enter loan amount --> "))
loan_period = eval(input("Enter loan period in years --> "))
loan_period *= 12
balance = loan 
principal = loan / loan_period
print("Payment Schedule")
print("MONTH\t|\tPRINCIPAL\t|REMAINING BALANCE\t|\tINTEREST\t|\tMONTHLY PAYMENT\t|")

for i in range(1,loan_period + 1):
    balance -= principal
    interest = balance * 0.03
    monthly = principal + interest 


    print(f"{i}\t|\t{round(principal,2)}\t\t|\t{round(balance,2)}\t\t|\t{round(interest,2)}\t\t|\t{round(monthly,2)}\t\t|")
