def tri():
    a,b,c=1,2,int(input("Please enter the highest number you would like to go up to: "))
    while b<c+2:
        print(a,b-1)
        a,b=a+b,b+1
    print("\n")
    tri()
tri()



