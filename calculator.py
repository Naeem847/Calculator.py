balance=0.0
def show_balance():
     global balance
     print(f"\nyour current balance is ${balance:2f}")
def deposit():
    global balance
    amount=float(input("deposite the balance:"))
    if amount>0:
        balance+=amount
        print(f"${balance:2f} depoosite is sucessfully!")
    else:
        print("invalid balance please try again") 
def withdraw():
    global balance
    amount=float(input("withdraw the balance"))
    if 0<amount<=balance:
         balance-=amount
         print(f"${balance:2f} withdraw successfully!")
    else:
        print("insufficient balance or inlid service")
def exit():
    
    print("thank you for using our service!")
    
def main():
    while True:
        print("\n___simple bank menu___")
        print("1.show_balance") 
        print("2.deposite")
        print("3.withdraw")
        print("4.exit")
        choice=int(input("enter the menu from 1 to 4\n"))
        if choice==1:
         show_balance()
        elif choice==2:
         deposit()
        elif choice==3:
         withdraw()
        elif choice==4:
          exit()
        break
              
    else:
         print("invalid choice please try again:")
if __name__ == "__main__":
    main()          
