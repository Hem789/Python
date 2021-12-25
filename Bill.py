i=1
li=[]
sum=0
print("Enter numbers to add or ""q"" to exit")
while(True):
    x=input()
    if x=="q":
        input("\nYour bill is ready\nPress enter to see your bill \n\n")
        break
    else:
        try:
            price=float(x)
            li.append(price)
            sum+=price
        except:
            print("You can either enter number or q only...")
            continue
print("SriRam Verma Store")
for items in li:
    print(str(i)+". ",items)
    i+=1
print("your total amount is:",sum)
print("Thank you for your visit")
input("press enter to exit")
