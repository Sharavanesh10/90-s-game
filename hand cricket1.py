import random
score = 0
pc = 0
def batting():
    global score
    score = 0
    
    while True:
        user_input = int(input("Enter your number: "))
        if(user_input>0 or user_input<6):
            print('invalid value')
            continue
        computer_input = random.randint(1, 6)
        print("Computer's number:", computer_input)
    
        if user_input == computer_input:
            print("You are out!")
            break
        else:
            score += user_input
            print("Your score:", score)
            if score > pc and pc != 0:
                break
    print("Your final score:", score+1)
def bowling() :
    global pc
    pc=0
    global score
    while True:
        user_input=int(input("bowl:"))
        if(user_input>0 or user_input<6):
            print('invalid value')
            continue
        computer_input=random.randint(1,6)
        print("computer score:",computer_input)
        if(computer_input==user_input):
            print("computer is out")
            break
        else:
            pc += computer_input
            print("pc score:",pc)
            if score < pc and score != 0:
                break
    print("pc final score is",pc)
while True:
    choice=input("enter your choice to bat or bowl:")

    
    if(choice =='bowl'):
        bowling()
        batting()
        if(score==pc):
            print("match tie")
        elif(score>pc):
            print("won")
        else:
            print("lost")
    elif(choice =='bat'):
        batting()

        bowling()
    
        if(score==pc):
            print("match tie")
        elif(score>pc):
            print("won")
        else:
            print("lost")
    else:
        print("invalid option")
        continue
     
        
    



