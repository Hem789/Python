def seri(n):
    a=0
    b=1
    print(a)
    print(b)
    for item in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c
        
x=int(input("enter number of terms\n"))
seri(x)