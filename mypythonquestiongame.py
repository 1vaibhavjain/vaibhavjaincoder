permission=(input("do you want to play this game: yes or no :"))
if(permission=="yes"):
    print("you enter into the quiz")
    print("please choose any one topic :")
    print("1. science")
    print("2. entertainment")
    print("3. sports")
    enter_the_topic=int(input("enter the option :"))
    if(enter_the_topic==2):
        print("question 1. which song is being sung by musician AURORA ")
        print("1. runaway")
        print("2. despercito")
        print("3. my way")
        print("4. non of those")
        chose_opiton=int(input("choose the answer :"))
        if (chose_opiton==1):
            point1=10
            print("correct you got ",point1, "marks")
        else:
            point1=0
            print("incorrect you got ",point1)
    
        print("question 2. cannes film fest is held in ")
        print("1. italy")
        print("2. france")
        print("3. germany")
        print("4. england")
        chose_opiton=int(input("choose the answer :"))
        if (chose_opiton==2):
            point2=10
            print("correct you got ",point2, "marks")
        else:
            point2=0
            print("incorrect you got ",point2)
        print("question 3.who was the first recipient of dada saheb phalke award? ")
        print("1. kanan devi")
        print("2. amir khan")
        print("3. sanjay")
        print("4. devika rani")
        chose_opiton=int(input("choose the answer :"))
        if (chose_opiton==4):
            point3=10
            print("correct you got ",point3, "marks")
        else:
            point3=0

            print("incorrect you got ",point3)
        print("question 4. who is the director of movie bahubali 2 ")
        print("1. telefilm")
        print("2. salman films")
        print("3. rajamouli")
        print("4. sanjaylella bansali")

        chose_opiton=int(input("choose the answer :"))
        if (chose_opiton==3):
            point4=10
            print("correct you got ",point4, "marks")
        else:
            point4=0
            print("incorrect you got ",point4)
    total= point1+point2+point3+point4
    print("=============you score",total,"out of 40===============")
    
else :
    print("not able to play this quiz")
    
        
        
                  
