import random
PLAYER_2=0
TOTAL=100
TOTAL_PLAYER_1=50
TOTAL_PLAYER_2=50
print("you both have 50 beats each")
def oddoreven(value):
    if(value%2==0):
        return 2
    else:
        return 1
def you_won(total_1,total_2,chall):
    total_2-=chall
    total_1+=chall
    return total_1,total_2
def you_loss(total_1,total_2,chall):
    total_1-=chall
    total_2+=chall
    return total_1,total_2
    
START=1
while(TOTAL_PLAYER_1+TOTAL_PLAYER_2<=TOTAL):
    if(START==1):
        COM_CHALL=random.randrange(1,50)-PLAYER_2
        your_guess=eval(input("your guess (single=1 or double=2):"))
        temp_var=oddoreven(COM_CHALL)
        #if(COM_CHALL<TOTAL_PLAYER_2):
        if(temp_var==your_guess):
            print("you won")
            print("computer challenged with you :",COM_CHALL)
            TOTAL_PLAYER_1,TOTAL_PLAYER_2=you_won(TOTAL_PLAYER_1,TOTAL_PLAYER_2,COM_CHALL)
            print("you left with")
            #PLAYER_2=COM_CHALL
        else:
            print("you died")
            print("computer challenged with you :",COM_CHALL)
            TOTAL_PLAYER_1,TOTAL_PLAYER_2=you_loss(TOTAL_PLAYER_1,TOTAL_PLAYER_2,COM_CHALL)
        COM_CHALL=0
        START=2
        #else:
            #print("again start")
            #START=1

    if(START==2):
        print("you left with --> ",TOTAL_PLAYER_1)
        COM_CHALL=int(input("your choice to challenge :"))
        your_guess=random.randrange(1,2)
        temp_var=oddoreven(COM_CHALL)
        #if(COM_CHALL<=TOTAL_PLAYER_1):
        if(temp_var==your_guess):
            print("you died")
            TOTAL_PLAYER_1,TOTAL_PLAYER_2=you_loss(TOTAL_PLAYER_1,TOTAL_PLAYER_2,COM_CHALL)
        else:
            print("you won")
            TOTAL_PLAYER_1,TOTAL_PLAYER_2=you_won(TOTAL_PLAYER_1,TOTAL_PLAYER_2,COM_CHALL)
            print("computer guess was---> ",your_guess)
        print("computer left with -->",TOTAL_PLAYER_2)
        COM_CHALL=0
        START=1
else:
    if(TOTAL_PLAYER_1<0):
        print("player_2 won")
    else:
        print("player_1 won")
                
        """else:
            print("again start")
            START=2"""
            



