while(True):
    i=1
    n=int(input("Enter a number: "))
    bull=input("Enter bool 1 for true and 0 for false: ")

    if bull=="1":
        while(i<=n):
            j=1
            while(j<=i):
                print("*",end="")
                j+=1
            i+=1
            print("")

    elif bull=="0":
        while(i<=n):
            j=n
            while(j>=i):
                print("*",end="")
                j-=1
            i+=1
            print("")

    else: 
        print("\nYOU CAN ENTER ONLY 0 OR 1 AS BOOL...")
        input("press enter to exit")
        break

    c=input("\nwould u like to continue?(y/n)")
    if(c=="y" or c=="Y"):continue
    elif(c=="n" or c=="N"):break
    else:
        input("\nYOU CAN INPUT ONLY Y OR N\npress enter to exit")
        break
