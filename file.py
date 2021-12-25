with open("D:/Testing/abc.txt","r+") as donkey:
    #print(donkey.read())
    donkey.write("you are not donkey anymore")
    print(donkey.read())
with open("D:/Testing/def.txt","w")as elephant:
    elephant.write("you are a dinosaur ")
    x=input("enter text to be added")
    elephant.write(x)