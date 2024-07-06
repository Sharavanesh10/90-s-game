import random as r
total=100
player_1_tot=50
player_2_tot=50
def oddoreven(value):
    if(value%2==0):
        return 2
    else:
        return 1
start=1
flag=1
while(player_1_tot > 0 and player_2_tot > 0):
    if(player_1_tot>0 and player_2_tot>0):
        if(start==1):
            chall=r.randrange(1,player_2_tot)
            your_guess=int(input("your guess (sigles=1 or double=2):"))
            temp_var=oddoreven(chall)
            if(temp_var==your_guess):
                print("you won")
                print("computer challenged with you :",chall)
                player_1_tot+=chall
                player_2_tot-=chall
                print("you left with --->",player_1_tot)
            else:
                print("you loss")
                print("computer challenged with you :",chall)
                player_1_tot-=chall
                player_2_tot+=chall
                print("you left with-->",player_1_tot)
            chall=0
            start=2
        if(start==2):
            print("you left with-->",player_1_tot)
            chall=int(input("your choice to challenge :"))
            your_guess=r.randrange(1,2)
            temp_var=oddoreven(chall)
            if(temp_var==your_guess):
                print("you loss")
                print("you challenged with computer :",chall)
                player_2_tot+=chall
                player_1_tot-=chall
                print("you left with --->",player_1_tot)
            else:
                print("you won")
                print("computer challenged with you :",chall)
                player_2_tot-=chall
                player_1_tot+=chall
                print("you left with-->",player_1_tot)
            chall=0
            start=1
    else:
        flag=0
        break
else:
    if(player_1_tot<0):
        print("player_2_won")
    else:
        print("player_1s_won")
        
            
    
