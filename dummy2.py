list1 = {1:5,2:5,3:5,4:5,5:5,6:5,7:5}
list2 = {8:5,9:5,10:5,11:5,12:5,13:5,14:5}
list3 = {**list1, **list2}
#print(list3)
       #for i in range(1): 
#    list1.append([]) 
 #   for j in range(7): 
  #      list1[i].append(j)
#for i in range(1): 
 #   list2.append([]) 
  #  for j in range(7): 
   #     list2[i].append(j)
#print(list1)
#print(list2)
def get():
    if(priority==1):
        select=int(input("Select the key from 1-7 :"))
        if(select<=7 and select>0):
            if (list1[select]==None):
                print("Select another key")
                get()
            else:
                return player1(select)
        else:
            print("Select another key")
            get()
    elif (priority==2):
        select=int(input("Select the key from 8-14 :"))
        if(select<=14 and select>7):
            if (list2[select]==None):
                print("Select another key")
                get()
            else:
                return player2(select)
        else:
            print("Select another key")
            get()
    else:
        get()

def player1(select):
    #value=1
    #select=int(input("Select the key from 1-7 :"))
    #if (list1[select]==None):
     #   print("Select another key")
    #else:
    dum=list3[select]
    list3[select] = 0
    for i in range(select+1,select+dum+1):
        list3[i]+=1
            #list1[select]=list1[select]+value
            
        print(list3)
def player2(select):
    #value=1
    #select=int(input("Select the key from 1-7 :"))
    #if (list1[select]==None):
     #   print("Select another key")
    #else:
    dum=list3[select]
    list3[select] = 0
    count = 0
    if select != 14:
        next_val = list3[select+1]
    else:
        next_val = list3[1]
    i = select
    while next_val != 0:
        if i < 14:
            list3[i]+=1
            count += 1
        else:
            i = 1
            dum = dum - count
            list3[1] += 1
            count += 1
            select = 1
        i += 1
        next_val = list3[i]
            #list1[select]=list1[select]+value
            
        print(list3)
priority=eval(input("player 1 or player 2:"))
if (priority==1):
    get()
else :
    get()

    
