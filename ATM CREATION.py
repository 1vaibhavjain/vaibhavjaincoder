print("=====WELCOME TO THE HDFC BANK======")
i=1
j=5000
password=4444
while(i<=j):
    print("1 withdraw money")
    print("2 update password")
    print("3 exit")
    chose_option= int(input("what you want to do :"))
    if(chose_option==1):
        total_ammount=30000000
        print("you have ",total_ammount,"in your account")
        money=int(input("how much money you want to withdrawl :"))
        if(money<=total_ammount):
            print("please collect your money :",money)
        else:
            print("you have unsufficient balance")
            break
        
        final_ammount=input("do you want to see your final ammount :")
        if (final_ammount=="yes"):
            final_ammount=total_ammount-money
            print("your balance is : ",final_ammount)
            
        else:
            print("thanku")
    elif(chose_option==2):
        print("=====update password=====")
        p2=int(input("enter your password :"))
        
        if(p2==password):
            print("you have enter the correct password :")
            newpassword=int(input("enter the new password :"))
            password=newpassword
            print("your password has been changed ",newpassword)
            
        else:
            print("you have enter wrong password :")


    elif(chose_option==3):
        print("====exit====")
        break

        
        
    

