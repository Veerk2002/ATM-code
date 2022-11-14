# print("welcome in ATM","\n")

bank=input("enter the Bank name: ")
if bank=="HDFC Bank" or bank=="PNB Bank" or bank=="ABC Bank":
    print("welcome to: ",bank)
    card=input("insert your card: ")
    if card=="credit" or card=="debit":
        print(card,"please insert credit card: ")
        l=input("select your language: ")
        if l=="english" or l=="hindi":
            print(l)
            amount=input("select the option: withdraw,transaction,quit: ")
            if amount=="withdraw":
                print("next")
            if amount=="transaction":
                print("next")
            if amount=="quit":
             print("stop")
            a=int(input("enter amount: "))
            if a>=200:
                print(a)
                account_type=input("select the type of account: ")
                if account_type=="current":
                    print(account_type)
                    print("next")
                    a_n=int((input("enter account no: ")))
                    if a_n>=0 and a_n<=17:
                        l=len(a_n)<=17
                    print(a_n)
                    c=input("choose you want to confirm or quit: ")
                    if c=="confirm":
                        print(c)
                        if c=="quit":
                         print(c)
                        R=input("receive your receipt choose yes or not: ")
                        if R=="yes":
                            print("your transaction is processing")
                            if R=="no":
                              print("remove your card")
                            p_c=int(input("pls enter the pin code: "))
                            if p_c>=0 and p_c<=4 and len(p_c)==4:
                                # p=len(p_c)==4
                             print(p_c)
                            else:
                              print("olny 4 digit allowed")        
                        else:
                            print("quit")
                    else:
                        print("quit")
                else:
                 print("you can recesive your money")
            else:
             print("only 17 no is included in your account no")
        else:
            print("transaction")
    else:
     print("withdraw your money")
else:
 print("pls select your bank name")