name=input("enter your name")
Balance=int(input("Enter a balances"))
transactions = []
def check_balances():
    print("your balances is ₹",Balance)
def amount():
    global Balance
    amount=int(input("enter a amount"))
    Balance=Balance + amount
    transactions.append(f"Deposit ₹,{Balance}")
    print("Deposit Successful\n","New Balances: Rs",Balance) 
def withdraw():
    global Balance
    amount=int(input("enter a amount"))
    if amount<=Balance:
        Balance = Balance - amount
        transactions.append(f"Withdraw ₹,{amount}")
        print("Remaining Balance",Balance)
    else:
        print("Insufficient Balance")    


def ministatement():

    print("\n========== MINI STATEMENT ==========")

    if len(transactions) == 0:
        print("No Transactions Yet")
    else:
        for t in transactions:
            print(t)

    print("-----------------------------------")
    print("Current Balance: ₹", Balance)    

while True:
    print("============ATM==========")
    print("1.Check Balance\n" 
          "2.Deposit\n"
          "3.withdraw\n"
          "4.mini statement\n"
          "5.exit")
    choice=int(input("enter a choice: "))
    if choice==1:
        check_balances()
    elif choice==2:
        amount()
    elif choice==3:
         withdraw()
    elif choice==4:
         ministatement()
    elif choice==5:
        print("Thank you for using our ATM 😊")
        break
    else:
        print("invaild choice")      
                        
