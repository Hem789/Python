na1=["apple","banana","orange"]
na2=["kick","punch","jump"]
while(True):
    def getdate():
        from datetime import datetime
        return datetime.now()
    log=input("press\n1 to log\n2 to retrive\nor q to exit\n:")
    if log=="Q" or log=="q":break
    elif(log!="1"and log!="2"):
        print("you can only enter 1 or 2 or q")
        continue
    
    else:
        ne=input("\npress\n1 for tom\n2 for Dick\n3 for Harry\n:")
        if(ne!="1" and ne!="2" and ne!="3"):
            print("You can only enter 1,2 or 3")
            continue
        else:
            name=int(ne)-1
            action=input("press\n1 for diet\n2 for exercise\n:")
            if action!="1"and action!="2":
                print("you can enter either 1 or 2 only")
                continue
            else:
                if log=="1":
                    sting=input("enter new data :")
                    if(action=="1"):na1[name]=sting
                    else:na2[name]=sting
                    print("stored successfully")
                else:
                    x=getdate()
                    if(action=="1"):print("[",x,"]->",na1[name])
                    else:print("[",x,"]->",na2[name])
                    continue