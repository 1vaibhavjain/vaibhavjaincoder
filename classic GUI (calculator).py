print("WELCOME TO SAITM CALCULATOR")
i=1
while(i>=0):
    print("1 simple calculation +,-,/,* ")
    print("2 find area of square , rectangle , triangle , circle ")
    print("3 volume of sphere , cylinder , cone ")
    print("4 EXIT")
    choose_option=int(input("what you want to do :"))
    if(choose_option==1):
        print("=======SIMPLE CALCULATION========")
        a=int(input("enter first number :"))
        b=int(input("enter second number :"))
        add=a+b
        sub=a-b
        mul=a*b
        div=a/b
        choose_the_calculation= input("what you wanna do add, sub,mul,div :")
        if(choose_the_calculation=="add"): 
            print("after adding two values you get :",add)
        elif(choose_the_calculation=="sub"):
            print("after subtracting two values you get :",sub)
        elif(choose_the_calculation=="mul"):
            print("after multiplying two values you get :",mul)
        elif(choose_the_calculation=="div"):
            print("after dividing two values you get :",div)
        else:
            break
        print("do you want to go back to main menue :")
        answer=input("yes/no")
        if(answer=="yes"):
            print("go ahead ")
            continue
        else:
            break
    elif(choose_option==2):
        print("======FIND THE AREA==========")
        choose_the_calculation= input("what you wanna do area of square, rectangle,triangle,circle :")
        if(choose_the_calculation=="square"):
            side=int(input("enter the side :"))
            square=side*side
            print("after area of square you get :",square)
        elif(choose_the_calculation=="rectangle"):
            length=int(input("enter the length :"))
            breadth=int(input("enter the breadth :"))
            rectangle=length*breadth
            print("after area of rectangle you get :",rectangle)
        elif(choose_the_calculation=="triangle"):
            base=int(input("enter the base :"))
            height=int(input("enter the height :"))
            triangle=0.5*base*height
            print("after area of triangle you get  :",triangle)
        elif(choose_the_calculation=="circle"):
            radious=int(input("enter the radious :"))
            circle=3.14*radious*radious
            print("after area of circle you get :",circle)
        print("do you want to go back to main menue :")
        answer=input("yes/no")
        if(answer=="yes"):
            print("go ahead ")
            continue
        else:
            break
    elif(choose_option==3):
        print("=======FIND THE VOLUME========")
        choose_the_calculation= input("what you wanna do volume of sphere , cylinder , cone :")
        if(choose_the_calculation=="sphere"):
            radious=int(input("enter the radious :"))
            sphere=(4/3)*3.14*(radious**3)
            print("volume of sphere :",sphere)
        elif(choose_the_calculation=="cylinder"):
            radious=int(input("enter the radious :"))
            height=int(input("enter the height :"))
            cylinder=3.14*(radious**2)*height
            print("volume of cylinder :",cylinder)
        elif(choose_the_calculation=="cone"):
            radious=int(input("enter the radious :"))
            height=int(input("enter the height :"))
            cone=(1/3)*3.14*(radious**2)*height
            print("volume of cone :",cone)
        print("do you want to go back to main menue :")

        answer=input("yes/no")
        if(answer=="yes"):
            print("go ahead ")
            continue
        else:
            break
    elif(choose_option==4):
        print("=======EXIT======")
    i+=1
   
    
